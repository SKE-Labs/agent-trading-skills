#!/usr/bin/env python3
"""Validate and atomically synchronize the curated trading-skill catalogue."""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path
from typing import Any

import requests
import yaml

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
BASEMENT_API_URL = "https://basement.deepalpha.mn"
SYNC_SOURCE = "github:SKE-Labs/agent-trading-skills"
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
ASSET_EXTENSIONS = {
    ".md",
    ".py",
    ".js",
    ".ts",
    ".sh",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".webp",
    ".json",
    ".csv",
    ".tsv",
    ".parquet",
    ".txt",
    ".yaml",
    ".yml",
}


class SyncError(RuntimeError):
    """A validation or remote sync failure."""


def sha256(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def parse_skill_document(path: Path) -> tuple[dict[str, Any], str]:
    if path.is_symlink():
        raise SyncError(f"Symlinked SKILL.md is not allowed: {path}")
    document = path.read_text(encoding="utf-8")
    match = re.match(r"^---\r?\n([\s\S]*?)\r?\n---(?:\r?\n|$)", document)
    if not match:
        raise SyncError(f"Malformed YAML frontmatter: {path}")
    try:
        frontmatter = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        raise SyncError(f"Invalid YAML in {path}: {exc}") from exc
    if not isinstance(frontmatter, dict):
        raise SyncError(f"Frontmatter must be a mapping: {path}")
    name = frontmatter.get("name")
    description = frontmatter.get("description")
    if not isinstance(name, str) or not SLUG_RE.fullmatch(name):
        raise SyncError(f"Invalid frontmatter name in {path}")
    if not isinstance(description, str) or not description.strip():
        raise SyncError(f"Missing frontmatter description in {path}")
    if len(document.encode("utf-8")) > 256 * 1024:
        raise SyncError(f"SKILL.md exceeds 256 KiB: {path}")
    return frontmatter, document


def build_asset(path: Path, skill_dir: Path) -> dict[str, str]:
    if path.is_symlink():
        raise SyncError(f"Symlinked assets are not allowed: {path}")
    relative = path.relative_to(skill_dir).as_posix()
    if path.suffix.lower() not in ASSET_EXTENSIONS:
        raise SyncError(f"Unsupported asset extension: {path}")
    content = path.read_bytes()
    if len(content) > 1024 * 1024:
        raise SyncError(f"Asset exceeds 1 MiB: {path}")
    return {
        "path": relative,
        "sha256": sha256(content),
        "content_base64": base64.b64encode(content).decode("ascii"),
    }


def discover_skills(skills_dir: Path = SKILLS_DIR) -> list[dict[str, Any]]:
    if not skills_dir.is_dir():
        raise SyncError(f"Skills directory does not exist: {skills_dir}")
    documents = sorted(skills_dir.glob("*/*/SKILL.md"))
    nested_documents = sorted(skills_dir.rglob("SKILL.md"))
    if documents != nested_documents:
        unexpected = sorted(set(nested_documents) - set(documents))
        raise SyncError(
            f"SKILL.md must use skills/<category>/<slug> layout: {unexpected}"
        )
    if not documents:
        raise SyncError("No SKILL.md files found")

    skills: list[dict[str, Any]] = []
    seen: set[str] = set()
    for document_path in documents:
        category = document_path.parent.parent.name
        directory_slug = document_path.parent.name
        frontmatter, document = parse_skill_document(document_path)
        slug = frontmatter["name"]
        if slug != directory_slug:
            raise SyncError(
                f"Directory '{directory_slug}' does not match frontmatter name '{slug}'"
            )
        if slug in seen:
            raise SyncError(f"Duplicate skill slug: {slug}")
        seen.add(slug)
        asset_paths = sorted(
            path
            for path in document_path.parent.rglob("*")
            if path.is_file() and path != document_path
        )
        assets = [build_asset(path, document_path.parent) for path in asset_paths]
        skills.append(
            {
                "slug": slug,
                "document": document,
                "tags": [category],
                "assets": assets,
            }
        )
    return sorted(skills, key=lambda skill: skill["slug"])


def build_request(skills: list[dict[str, Any]], *, dry_run: bool) -> dict[str, Any]:
    required = {
        "SUPABASE_SERVICE_KEY": os.environ.get("SUPABASE_SERVICE_KEY"),
        "MARKETPLACE_AUTHOR_ID": os.environ.get("MARKETPLACE_AUTHOR_ID"),
        "GITHUB_SHA": os.environ.get("GITHUB_SHA"),
        "GITHUB_RUN_ID": os.environ.get("GITHUB_RUN_ID"),
        "GITHUB_RUN_ATTEMPT": os.environ.get("GITHUB_RUN_ATTEMPT"),
    }
    missing = [name for name, value in required.items() if not value]
    if missing:
        raise SyncError(f"Missing required environment variables: {', '.join(missing)}")
    if not re.fullmatch(r"[0-9a-f]{40}", required["GITHUB_SHA"] or ""):
        raise SyncError("GITHUB_SHA must be a 40-character lowercase git SHA")
    return {
        "schema_version": 2,
        "source": SYNC_SOURCE,
        "source_revision": required["GITHUB_SHA"],
        "source_run_id": required["GITHUB_RUN_ID"],
        "source_run_attempt": int(required["GITHUB_RUN_ATTEMPT"] or "0"),
        "author_id": required["MARKETPLACE_AUTHOR_ID"],
        "dry_run": dry_run,
        "skills": skills,
    }


def request_json(
    session: requests.Session,
    method: str,
    url: str,
    *,
    token: str,
    payload: dict[str, Any] | None = None,
) -> dict[str, Any]:
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    last_error: Exception | None = None
    for attempt in range(1, 4):
        try:
            response = session.request(
                method,
                url,
                headers=headers,
                json=payload,
                timeout=(10, 120),
            )
            if response.status_code in {429, 502, 503, 504} and attempt < 3:
                time.sleep(attempt)
                continue
            if response.status_code != 200:
                raise SyncError(
                    f"Basement returned HTTP {response.status_code}: {response.text[:1000]}"
                )
            data = response.json()
            if not isinstance(data, dict):
                raise SyncError("Basement returned a non-object JSON response")
            return data
        except (requests.ConnectionError, requests.Timeout) as exc:
            last_error = exc
            if attempt < 3:
                time.sleep(attempt)
                continue
    raise SyncError(f"Basement request failed after three attempts: {last_error}")


def validate_response(
    data: dict[str, Any], *, dry_run: bool, expected_slugs: set[str]
) -> dict[str, Any]:
    if data.get("code") != 0 or not isinstance(data.get("response"), dict):
        raise SyncError(
            f"Invalid Basement response envelope: {json.dumps(data)[:1000]}"
        )
    response = data["response"]
    results = response.get("results")
    if response.get("dry_run") is not dry_run or not isinstance(results, list):
        raise SyncError("Basement response does not match the requested sync mode")
    catalog_hash = response.get("catalog_sha256")
    if not isinstance(catalog_hash, str) or not re.fullmatch(
        r"[0-9a-f]{64}", catalog_hash
    ):
        raise SyncError("Basement returned an invalid catalogue hash")
    if not all(isinstance(result, dict) for result in results):
        raise SyncError("Basement returned a malformed result entry")
    non_archive = [
        result
        for result in results
        if result.get("status") not in {"archived", "would-archive"}
    ]
    actual_slugs = [result.get("slug") for result in non_archive]
    if not all(isinstance(slug, str) for slug in actual_slugs):
        raise SyncError("Basement returned a desired-skill result without a slug")
    if len(actual_slugs) != len(set(actual_slugs)):
        raise SyncError("Basement returned duplicate desired-skill results")
    if set(actual_slugs) != expected_slugs:
        raise SyncError(
            "Basement desired-skill results do not match the submitted catalogue: "
            f"expected {sorted(expected_slugs)}, received {sorted(actual_slugs)}"
        )
    allowed = (
        {
            "would-create",
            "would-adopt",
            "would-update",
            "would-republish",
            "would-archive",
            "up-to-date",
        }
        if dry_run
        else {"created", "adopted", "updated", "republished", "archived", "up-to-date"}
    )
    invalid = [result for result in results if result.get("status") not in allowed]
    if invalid:
        raise SyncError(f"Unexpected sync statuses: {invalid}")
    return response


def print_summary(response: dict[str, Any]) -> None:
    summary = response.get("summary", {})
    counts = ", ".join(f"{key}={value}" for key, value in summary.items() if value)
    print(f"catalog_sha256={response.get('catalog_sha256')} {counts or 'no changes'}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--validate-only", action="store_true")
    parser.add_argument("--dry-run-only", action="store_true")
    args = parser.parse_args()
    try:
        skills = discover_skills()
        expected_slugs = {skill["slug"] for skill in skills}
        asset_count = sum(len(skill["assets"]) for skill in skills)
        encoded_size = len(json.dumps({"skills": skills}).encode("utf-8"))
        if encoded_size > 2 * 1024 * 1024:
            raise SyncError(
                f"Encoded catalogue exceeds Basement's 2 MiB limit: {encoded_size}"
            )
        print(
            f"Validated {len(skills)} skills and {asset_count} assets ({encoded_size} bytes JSON)"
        )
        if args.validate_only:
            return 0

        token = os.environ.get("SUPABASE_SERVICE_KEY", "")
        session = requests.Session()
        sync_url = f"{BASEMENT_API_URL}/api/v1/marketplace/sync"
        dry_payload = build_request(skills, dry_run=True)
        plan = validate_response(
            request_json(session, "POST", sync_url, token=token, payload=dry_payload),
            dry_run=True,
            expected_slugs=expected_slugs,
        )
        print("Dry-run plan:")
        print_summary(plan)
        if args.dry_run_only:
            return 0

        apply_payload = dict(dry_payload)
        apply_payload["dry_run"] = False
        applied = validate_response(
            request_json(session, "POST", sync_url, token=token, payload=apply_payload),
            dry_run=False,
            expected_slugs=expected_slugs,
        )
        if applied.get("catalog_sha256") != plan.get("catalog_sha256"):
            raise SyncError("Dry-run and apply catalogue hashes differ")
        print("Applied catalogue:")
        print_summary(applied)
        return 0
    except (SyncError, ValueError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
