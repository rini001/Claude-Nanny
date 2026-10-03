import json
from pathlib import Path


session_file = (
    Path.home()
    / ".claude"
    / "projects"
    / "c--Users-Dell-Desktop-New-folder--5--shiftninja-client"
    / "dbee4e39-57f3-4028-870a-f955e5d3678d.jsonl"
)

with open(session_file, "r", encoding="utf-8") as file:
    for line in file:
        record = json.loads(line)

        message = record.get("message")

        if not isinstance(message, dict):
            continue

        role = message.get("role")

        if role == "assistant":
            print(json.dumps(message, indent=2)[:8000])
            break