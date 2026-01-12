from pathlib import Path


def clean_markdown(input_path, output_path):
    input_path = Path(input_path)
    output_path = Path(output_path)

    cleaned_lines = []

    with input_path.open("r", encoding="utf-8") as f:
        for line in f:
            stripped = line.lstrip()

            # Skip plain bullet points like "- item"
            if stripped.startswith("- ") and not stripped.startswith("- ["):
                continue

            cleaned_lines.append(line)

    with output_path.open("w", encoding="utf-8") as f:
        f.writelines(cleaned_lines)


if __name__ == "__main__":
    clean_markdown("model_checklist.md", "model_checklist_minimal.md")
