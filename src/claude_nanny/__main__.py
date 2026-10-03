from pathlib import Path

from claude_nanny.reader import SessionReader


def main():
    session_file = (
        Path.home()
        / ".claude"
        / "projects"
        / "c--Users-Dell-Desktop-New-folder--5--shiftninja-client"
        / "025242dd-ddfc-4866-9a30-60b92b8c450e.jsonl"
    )

    reader = SessionReader()

    messages = reader.read_messages(session_file)

    print(f"Found {len(messages)} messages\n")

    for message in messages[:10]:
        print(f"[{message.role}]")
        print(message.content)
        print("-" * 50)


if __name__ == "__main__":
    main()