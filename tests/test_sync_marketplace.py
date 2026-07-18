from __future__ import annotations

import importlib.util
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "sync-marketplace.py"
SPEC = importlib.util.spec_from_file_location("sync_marketplace", SCRIPT)
assert SPEC and SPEC.loader
sync = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(sync)


class CatalogueRegressionTests(unittest.TestCase):
    def test_current_catalogue_is_complete_and_keeps_documents_and_assets(self):
        skills = sync.discover_skills()
        self.assertEqual(len(skills), 56)
        self.assertEqual(sum(len(skill["assets"]) for skill in skills), 3)
        self.assertTrue(all(skill["document"].startswith("---\n") for skill in skills))
        paths = {asset["path"] for skill in skills for asset in skill["assets"]}
        self.assertEqual(
            paths,
            {
                "references/PATTERNS.md",
                "scripts/calculate_position.py",
                "scripts/calculate_fibonacci.py",
            },
        )

    def test_directory_and_frontmatter_name_must_match(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            skill_dir = root / "category" / "directory-name"
            skill_dir.mkdir(parents=True)
            (skill_dir / "SKILL.md").write_text(
                "---\nname: another-name\ndescription: test\n---\nbody\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(sync.SyncError, "does not match"):
                sync.discover_skills(root)

    def test_unknown_asset_extensions_fail_closed(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            skill_dir = root / "category" / "valid-name"
            skill_dir.mkdir(parents=True)
            (skill_dir / "SKILL.md").write_text(
                "---\nname: valid-name\ndescription: test\n---\nbody\n",
                encoding="utf-8",
            )
            (skill_dir / "payload.exe").write_bytes(b"unsafe")
            with self.assertRaisesRegex(sync.SyncError, "Unsupported asset"):
                sync.discover_skills(root)


class RequestContractTests(unittest.TestCase):
    @patch.dict(
        os.environ,
        {
            "SUPABASE_SERVICE_KEY": "legacy-service-role-jwt",
            "MARKETPLACE_AUTHOR_ID": "00000000-0000-4000-8000-000000000001",
            "GITHUB_SHA": "a" * 40,
            "GITHUB_RUN_ID": "123",
            "GITHUB_RUN_ATTEMPT": "2",
        },
        clear=True,
    )
    def test_builds_v2_source_and_stale_run_contract(self):
        payload = sync.build_request([], dry_run=True)
        self.assertEqual(payload["schema_version"], 2)
        self.assertEqual(payload["source"], sync.SYNC_SOURCE)
        self.assertEqual(payload["source_run_id"], "123")
        self.assertEqual(payload["source_run_attempt"], 2)
        self.assertTrue(payload["dry_run"])

    def test_rejects_partial_success_envelopes(self):
        data = {
            "code": 0,
            "response": {
                "dry_run": False,
                "catalog_sha256": "a" * 64,
                "results": [{"slug": "one", "status": "updated"}],
            },
        }
        with self.assertRaisesRegex(sync.SyncError, "do not match"):
            sync.validate_response(data, dry_run=False, expected_slugs={"one", "two"})

    def test_rejects_duplicate_or_invalid_hash_responses(self):
        duplicate = {
            "code": 0,
            "response": {
                "dry_run": False,
                "catalog_sha256": "a" * 64,
                "results": [
                    {"slug": "one", "status": "updated"},
                    {"slug": "one", "status": "up-to-date"},
                ],
            },
        }
        with self.assertRaisesRegex(sync.SyncError, "duplicate"):
            sync.validate_response(duplicate, dry_run=False, expected_slugs={"one"})

        duplicate["response"]["catalog_sha256"] = "not-a-hash"
        with self.assertRaisesRegex(sync.SyncError, "catalogue hash"):
            sync.validate_response(duplicate, dry_run=False, expected_slugs={"one"})


if __name__ == "__main__":
    unittest.main()
