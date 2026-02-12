#!/usr/bin/env python3
"""Sync trading skills to the Basement marketplace.

Parses all SKILL.md files, extracts YAML frontmatter and content,
then POSTs to the Basement marketplace sync endpoint.

Required environment variables:
  BASEMENT_API_URL   - Basement API base URL (e.g. https://basement.embient.ai)
  SUPABASE_SERVICE_KEY - Supabase service role key (used as Bearer token)
  AUTHOR_ID          - UUID of the marketplace author for these skills
"""

import json
import os
import sys
from pathlib import Path

import requests
import yaml

SKILLS_DIR = Path(__file__).resolve().parent.parent / "skills"


def parse_skill_md(filepath: Path) -> dict | None:
    """Parse a SKILL.md file into frontmatter + content."""
    text = filepath.read_text(encoding="utf-8")

    if not text.startswith("---"):
        print(f"  SKIP {filepath} (no YAML frontmatter)")
        return None

    # Split on the second '---' delimiter
    parts = text.split("---", 2)
    if len(parts) < 3:
        print(f"  SKIP {filepath} (malformed frontmatter)")
        return None

    frontmatter = yaml.safe_load(parts[1])
    content = parts[2].strip()

    if not frontmatter or "name" not in frontmatter:
        print(f"  SKIP {filepath} (missing 'name' in frontmatter)")
        return None

    return {
        "frontmatter": frontmatter,
        "content": content,
    }


def build_skill_payload(
    filepath: Path, parsed: dict, category: str
) -> dict:
    """Build the sync payload for a single skill."""
    fm = parsed["frontmatter"]
    name = fm["name"]
    description = fm.get("description", "")
    metadata = {}

    # Preserve metadata fields from frontmatter
    if "license" in fm:
        metadata["license"] = fm["license"]
    if "metadata" in fm and isinstance(fm["metadata"], dict):
        metadata.update(fm["metadata"])

    tags = [category]

    return {
        "slug": name,
        "name": name,
        "description": description,
        "content": parsed["content"],
        "metadata": metadata,
        "tags": tags,
    }


def main():
    api_url = os.environ.get("BASEMENT_API_URL")
    service_key = os.environ.get("SUPABASE_SERVICE_KEY")
    author_id = os.environ.get("AUTHOR_ID")

    if not api_url or not service_key or not author_id:
        print("ERROR: Missing required environment variables")
        print("  BASEMENT_API_URL, SUPABASE_SERVICE_KEY, AUTHOR_ID")
        sys.exit(1)

    # Find all SKILL.md files
    skill_files = sorted(SKILLS_DIR.rglob("SKILL.md"))
    print(f"Found {len(skill_files)} skill files")

    skills = []
    for filepath in skill_files:
        # Extract category from directory path: skills/<category>/<skill-name>/SKILL.md
        relative = filepath.relative_to(SKILLS_DIR)
        parts = relative.parts
        category = parts[0] if len(parts) >= 2 else "uncategorized"

        parsed = parse_skill_md(filepath)
        if parsed:
            payload = build_skill_payload(filepath, parsed, category)
            skills.append(payload)
            print(f"  OK {payload['slug']} [{category}]")

    if not skills:
        print("No skills to sync")
        sys.exit(0)

    # POST to Basement sync endpoint in batches to avoid payload size limits
    sync_url = f"{api_url.rstrip('/')}/api/v1/marketplace/sync"
    batch_size = 10
    all_results = []

    print(f"\nSyncing {len(skills)} skills to {sync_url} (batches of {batch_size})")

    for i in range(0, len(skills), batch_size):
        batch = skills[i : i + batch_size]
        batch_num = i // batch_size + 1
        total_batches = (len(skills) + batch_size - 1) // batch_size
        print(f"  Batch {batch_num}/{total_batches} ({len(batch)} skills)...")

        response = requests.post(
            sync_url,
            json={"author_id": author_id, "skills": batch},
            headers={
                "Authorization": f"Bearer {service_key}",
                "Content-Type": "application/json",
            },
            timeout=60,
        )

        if response.status_code != 200:
            print(f"ERROR: Batch {batch_num} failed with status {response.status_code}")
            print(response.text)
            sys.exit(1)

        data = response.json()
        all_results.extend(data.get("response", []))

    # Print summary
    created = sum(1 for r in all_results if r["status"] == "created")
    updated = sum(1 for r in all_results if r["status"] == "updated")
    errors = [r for r in all_results if r["status"] == "error"]

    print(f"\nResults: {created} created, {updated} updated, {len(errors)} errors")

    for err in errors:
        print(f"  ERROR {err['slug']}: {err.get('error', 'unknown')}")

    if errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
