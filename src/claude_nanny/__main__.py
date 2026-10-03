from pathlib import Path

from claude_nanny.discovery import SessionDiscovery
from claude_nanny.reader import SessionReader
from claude_nanny.handoff_generator import (
    HandoffGenerator,
)
from claude_nanny.file_writer import (
    FileWriter,
)


def main():

    discovery = SessionDiscovery()

    project_dir = (
        discovery.get_latest_active_project()
    )

    session_files = (
        discovery.get_sessions_for_today(
            project_dir
        )
    )

    print(
        f"Found {len(session_files)} sessions today"
    )

    reader = SessionReader()

    all_messages = []

    for session_file in session_files:

        messages = (
            reader.read_messages(
                session_file
            )
        )

        all_messages.extend(
            messages
        )

    all_messages.sort(
        key=lambda message: (
            message.timestamp
        )
    )

    print(
        f"Total messages: {len(all_messages)}"
    )

    generator = HandoffGenerator()

    handoff = generator.generate(
        all_messages
    )

    writer = FileWriter()

    output_path = Path(
        "handoffs/latest.md"
    )

    writer.save_handoff(
        handoff,
        output_path,
    )

    print(
        f"Saved: {output_path}"
    )


if __name__ == "__main__":
    main()