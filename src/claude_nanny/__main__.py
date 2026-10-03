from claude_nanny.discovery import SessionDiscovery
from claude_nanny.reader import SessionReader
from claude_nanny.summarizer import create_summary


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

    print(create_summary(messages))


if __name__ == "__main__":
    main()