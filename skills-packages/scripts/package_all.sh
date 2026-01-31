#!/bin/bash
# Package all skills into .skill files

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_DIR="$(dirname "$SCRIPT_DIR")"
OUTPUT_DIR="${SKILLS_DIR}/dist"

mkdir -p "$OUTPUT_DIR"

echo "Packaging all skills..."
echo ""

for skill_dir in "$SKILLS_DIR"/*/; do
    skill_name=$(basename "$skill_dir")

    # Skip non-skill directories
    if [[ "$skill_name" == "scripts" ]] || [[ "$skill_name" == "dist" ]]; then
        continue
    fi

    # Check if SKILL.md exists
    if [[ -f "${skill_dir}SKILL.md" ]]; then
        echo "Packaging: $skill_name"
        python3 "$SCRIPT_DIR/package_skill.py" "$skill_dir" "$OUTPUT_DIR"
        echo ""
    fi
done

echo "Done! All packages are in: $OUTPUT_DIR"
ls -la "$OUTPUT_DIR"/*.skill 2>/dev/null || echo "No .skill files created"
