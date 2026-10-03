from claude_nanny.discovery import SessionDiscovery
from claude_nanny.reader import SessionReader


def main():
    discovery = SessionDiscovery()

    project = discovery.get_latest_active_project()

    session_file = discovery.get_latest_session(
        project
    )

    print(f"Project: {project.name}")
    print(f"Session: {session_file.name}\n")

    reader = SessionReader()

    messages = reader.read_messages(
        session_file
    )

    print(f"Found {len(messages)} messages\n")

    for message in messages[-10:]:
        print(f"[{message.role}]")
        print(message.content)
        print("-" * 50)


if __name__ == "__main__":
    main()