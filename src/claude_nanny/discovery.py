from pathlib import Path


def find_claude_directory():
    claude_dir = Path.home() / ".claude"

    print(f"Looking for: {claude_dir}")

    if not claude_dir.exists():
        print("❌ Claude directory not found")
        return

    print("✅ Claude directory found")
    print("\nContents:")

    for item in claude_dir.iterdir():
        print(f" - {item.name}")


find_claude_directory()