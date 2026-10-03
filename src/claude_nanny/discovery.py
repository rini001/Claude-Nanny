from pathlib import Path
import json


def inspect_session_file():
    session_file = (
        Path.home()
        / ".claude"
        / "projects"
        / "c--Users-Dell-Desktop-New-folder--5--shiftninja-client"
        / "dbee4e39-57f3-4028-870a-f955e5d3678d.jsonl"
    )

    print(f"Reading:\n{session_file}\n")

    with open(session_file, "r", encoding="utf-8") as file:

        for index, line in enumerate(file):

            if index >= 5:
                break

            data = json.loads(line)

            print("=" * 80)
            print(f"Record {index + 1}")
            print(f"Type: {type(data)}")

            if isinstance(data, dict):
                print("\nKeys:")

                for key in data.keys():
                    print(f" - {key}")


inspect_session_file()