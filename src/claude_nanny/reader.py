import json
from pathlib import Path

from claude_nanny.models import Message


class SessionReader:

    def read_messages(self, session_file: Path) -> list[Message]:
        messages = []

        with open(session_file, "r", encoding="utf-8") as file:

            for line in file:
                try:
                    record = json.loads(line)

                    message_data = record.get("message")

                    if not isinstance(message_data, dict):
                        continue

                    role = message_data.get("role")
                    content = message_data.get("content")

                    if (
                        isinstance(role, str)
                        and isinstance(content, str)
                    ):
                        messages.append(
                            Message(
                                role=role,
                                content=content,
                            )
                        )

                except Exception:
                    continue

        return messages