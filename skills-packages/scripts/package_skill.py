#!/usr/bin/env python3
"""
Package a skill folder into a .skill file for distribution.

Usage:
    python package_skill.py <skill-folder> [output-dir]

Examples:
    python package_skill.py ./customer-support
    python package_skill.py ./sales ./dist
"""

import os
import sys
import zipfile
import yaml
import re
from pathlib import Path


def validate_skill(skill_path: Path) -> tuple[bool, list[str]]:
    """Validate a skill folder structure and content."""
    errors = []

    # Check SKILL.md exists
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        errors.append("Missing required file: SKILL.md")
        return False, errors

    # Read and validate SKILL.md
    content = skill_md.read_text()

    # Check for frontmatter
    if not content.startswith("---"):
        errors.append("SKILL.md must start with YAML frontmatter (---)")
        return False, errors

    # Extract frontmatter
    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        errors.append("Invalid YAML frontmatter format")
        return False, errors

    try:
        frontmatter = yaml.safe_load(match.group(1))
    except yaml.YAMLError as e:
        errors.append(f"Invalid YAML in frontmatter: {e}")
        return False, errors

    if not isinstance(frontmatter, dict):
        errors.append("Frontmatter must be a mapping")
        return False, errors

    # Check required fields
    if "name" not in frontmatter:
        errors.append("Frontmatter missing required field: name")
    if "description" not in frontmatter:
        errors.append("Frontmatter missing required field: description")

    # Check description quality
    if "description" in frontmatter:
        desc = frontmatter["description"]
        if not isinstance(desc, str):
            errors.append("Frontmatter field 'description' must be a string")
        else:
            if len(desc) < 50:
                errors.append("Description too short (should be at least 50 characters)")
            if "use when" not in desc.lower() and "trigger" not in desc.lower():
                errors.append("Description should include trigger phrases (e.g., 'Use when...')")

    # Check SKILL.md size
    lines = content.split("\n")
    if len(lines) > 500:
        errors.append(f"SKILL.md is {len(lines)} lines (recommended: under 500)")

    if errors:
        return False, errors

    return True, []


def package_skill(skill_path: Path, output_dir: Path) -> Path:
    """Package a skill folder into a .skill file."""
    skill_name = skill_path.name
    output_file = output_dir / f"{skill_name}.skill"

    with zipfile.ZipFile(output_file, "w", zipfile.ZIP_DEFLATED) as zf:
        for file_path in skill_path.rglob("*"):
            if file_path.is_file():
                arcname = file_path.relative_to(skill_path)
                zf.write(file_path, arcname)

    return output_file


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    skill_path = Path(sys.argv[1]).resolve()
    output_dir = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else skill_path.parent

    if not skill_path.is_dir():
        print(f"Error: {skill_path} is not a directory")
        sys.exit(1)

    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Validating skill: {skill_path.name}")
    valid, errors = validate_skill(skill_path)

    if errors:
        print("\nValidation issues:")
        for error in errors:
            print(f"  - {error}")
        if not valid:
            print("\nPackaging aborted due to errors.")
            sys.exit(1)
        print("\nProceeding with warnings...")
    else:
        print("  ✓ Validation passed")

    print("\nPackaging skill...")
    output_file = package_skill(skill_path, output_dir)
    print(f"  ✓ Created: {output_file}")

    # Show package contents
    with zipfile.ZipFile(output_file, "r") as zf:
        print(f"\nPackage contents ({len(zf.namelist())} files):")
        for name in sorted(zf.namelist())[:10]:
            print(f"  - {name}")
        if len(zf.namelist()) > 10:
            print(f"  ... and {len(zf.namelist()) - 10} more")


if __name__ == "__main__":
    main()
