from pathlib import Path
import json


def inspect_message_record():
    session_file = (
        Path.home()
        / ".claude"
        / "projects"
        / "c--Users-Dell-Desktop-New-folder--5--shiftninja-client"
        / "dbee4e39-57f3-4028-870a-f955e5d3678d.jsonl"
    )

    with open(session_file, "r", encoding="utf-8") as file:

        for line in file:
            data = json.loads(line)

            if "message" in data:

                print("=" * 80)
                print("FOUND MESSAGE RECORD")
                print("=" * 80)

                print(json.dumps(data, indent=2)[:5000])

                break


inspect_message_record()