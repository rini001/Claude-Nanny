from claude_nanny.discovery import SessionDiscovery
from claude_nanny.reader import SessionReader
from claude_nanny.handoff_generator import HandoffGenerator


def main():
    discovery = SessionDiscovery()

    project_dir = discovery.get_latest_active_project()

    session_file = discovery.get_latest_session(
        project_dir
    )

    reader = SessionReader()

    messages = reader.read_messages(
        session_file
    )

    generator = HandoffGenerator()

    handoff = generator.generate(messages)

    print(handoff)


if __name__ == "__main__":
    main()