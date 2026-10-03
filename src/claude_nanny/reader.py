import json
from pathlib import Path

from claude_nanny.models import Message


class SessionReader:

    def read_messages(
        self,
        session_file: Path,
    ) -> list[Message]:

        messages = []

        with open(
            session_file,
            "r",
            encoding="utf-8",
        ) as file:

            for line in file:

                try:
                    record = json.loads(line)

                    message_data = record.get(
                        "message"
                    )

                    if not isinstance(
                        message_data,
                        dict,
                    ):
                        continue

                    role = message_data.get(
                        "role"
                    )

                    content = message_data.get(
                        "content"
                    )

                    timestamp = record.get(
                        "timestamp",
                        "",
                    )

                    text_content = None

                    if isinstance(
                        content,
                        str,
                    ):
                        text_content = content

                    elif isinstance(
                        content,
                        list,
                    ):
                        text_parts = []

                        for item in content:

                            if (
                                isinstance(
                                    item,
                                    dict,
                                )
                                and item.get(
                                    "type"
                                )
                                == "text"
                            ):
                                text_parts.append(
                                    item.get(
                                        "text",
                                        "",
                                    )
                                )

                        text_content = (
                            "\n".join(
                                text_parts
                            )
                        )

                    if (
                        isinstance(
                            role,
                            str,
                        )
                        and text_content
                    ):
                        messages.append(
                            Message(
                                role=role,
                                content=text_content,
                                timestamp=timestamp,
                            )
                        )

                except Exception:
                    continue

        return messages