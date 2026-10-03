from pathlib import Path
import json


def inspect_session_files():
    sessions_dir = Path.home() / ".claude" / "sessions"

    json_files = list(sessions_dir.glob("*.json"))

    print(f"Found {len(json_files)} session files\n")

    for session_file in json_files:
        print("=" * 60)
        print(f"File: {session_file.name}")

        try:
            with open(session_file, "r", encoding="utf-8") as file:
                data = json.load(file)

            print(f"Type: {type(data)}")

            if isinstance(data, dict):
                print("\nKeys:")

                for key in data.keys():
                    print(f" - {key}")

        except Exception as error:
            print(f"Error: {error}")


inspect_session_files()