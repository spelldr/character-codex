#!/usr/bin/env python3
"""Validate avatar JSON files against the minimal required fields from avatar.schema.json.
This validator reads the schema's "required" array and checks that each required property exists in the avatar file.
It also checks that "last_updated" is an ISO date (YYYY-MM-DD).

Usage: python tools/validate_avatar.py path/to/avatar.json
"""
import json
import sys
from pathlib import Path
from datetime import datetime


def fail(msg: str):
    print("ERROR:", msg)
    sys.exit(2)


def main():
    if len(sys.argv) != 2:
        print("Usage: python tools/validate_avatar.py path/to/avatar.json")
        sys.exit(1)

    avatar_path = Path(sys.argv[1])
    if not avatar_path.exists():
        fail(f"File not found: {avatar_path}")

    schema_path = Path('apps/app-0-init/avatar.schema.json')
    if not schema_path.exists():
        fail(f"Schema file not found: {schema_path}")

    schema = json.loads(schema_path.read_text())
    avatar = json.loads(avatar_path.read_text())

    required = schema.get('required', [])
    errors = []

    for key in required:
        if key not in avatar:
            errors.append(f"Missing required property: {key}")

    # basic type checks for arrays where present
    for key in ('visual_deviations','behavioral_deviations','constraints','rendering_guidelines'):
        if key in avatar and not isinstance(avatar[key], list):
            errors.append(f"Property '{key}' must be an array")

    # last_updated date format
    if 'last_updated' in avatar:
        try:
            datetime.strptime(avatar['last_updated'], '%Y-%m-%d')
        except Exception:
            errors.append("'last_updated' must be in YYYY-MM-DD format")

    if errors:
        print(f"Validation failed for {avatar_path}:")
        for e in errors:
            print(' -', e)
        sys.exit(2)

    print(f"Validation OK: {avatar_path}")
    sys.exit(0)


if __name__ == '__main__':
    main()
