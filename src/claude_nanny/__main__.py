import sys
from datetime import date
from pathlib import Path

from claude_nanny.discovery import (
    SessionDiscovery,
)
from claude_nanny.reader import (
    SessionReader,
)
from claude_nanny.handoff_generator import (
    HandoffGenerator,
)
from claude_nanny.summary_generator import (
    SummaryGenerator,
)
from claude_nanny.file_writer import (
    FileWriter,
)


def get_output_path() -> Path:

    today = date.today().isoformat()

    return Path(
        f"handoffs/handoff_{today}.md"
    )


def load_today_messages():

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

        print(
            f"{session_file.name}: "
            f"{len(messages)} messages"
        )

        all_messages.extend(
            messages
        )

    all_messages.sort(
        key=lambda message:
        message.timestamp
    )

    print(
        f"Total messages: "
        f"{len(all_messages)}"
    )

    return all_messages


def run_summary():

    messages = load_today_messages()

    generator = SummaryGenerator()

    content = generator.generate(
        messages
    )

    writer = FileWriter()

    output_path = get_output_path()

    writer.save_handoff(
        content,
        output_path,
    )

    print(
        f"Saved: {output_path}"
    )


def run_handoff():

    messages = load_today_messages()

    generator = HandoffGenerator()

    content = generator.generate(
        messages
    )

    writer = FileWriter()

    output_path = get_output_path()

    writer.save_handoff(
        content,
        output_path,
    )

    print(
        f"Saved: {output_path}"
    )


def main():

    print("Claude Nanny")

    command = (
        sys.argv[1]
        if len(sys.argv) > 1
        else "summary"
    )

    if command == "summary":
        run_summary()

    elif command == "handoff":
        run_handoff()

    else:
        print(
            "Usage:"
        )
        print(
            "nanny summary"
        )
        print(
            "nanny handoff"
        )


if __name__ == "__main__":
    main()