from pathlib import Path
import json


def inspect_history_file():
    history_file = Path.home() / ".claude" / "history.jsonl"

    print(f"Reading: {history_file}\n")

    with open(history_file, "r", encoding="utf-8") as file:
        for index, line in enumerate(file):

            if index >= 3:
                break

            data = json.loads(line)

            print("=" * 80)
            print(f"Record {index + 1}\n")

            for key, value in data.items():
                print(f"{key}:")
                print(value)
                print()


inspect_history_file()