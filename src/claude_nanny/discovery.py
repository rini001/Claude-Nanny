from pathlib import Path
import json


def inspect_history_file():
    history_file = Path.home() / ".claude" / "history.jsonl"

    print(f"Reading: {history_file}")
    print()

    if not history_file.exists():
        print("History file not found")
        return

    with open(history_file, "r", encoding="utf-8") as file:
        for index, line in enumerate(file):

            if index >= 5:
                break

            try:
                data = json.loads(line)

                print("=" * 60)
                print(f"Line {index + 1}")

                if isinstance(data, dict):
                    print("Keys:")

                    for key in data.keys():
                        print(f" - {key}")

            except Exception as error:
                print(error)


inspect_history_file()