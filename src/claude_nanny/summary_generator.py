from claude_nanny.models import Message


class SummaryGenerator:

    def generate(
        self,
        messages: list[Message],
    ) -> str:

        lines = []

        lines.append("# Daily Summary")
        lines.append("")

        lines.append(
            f"Total messages: {len(messages)}"
        )

        lines.append("")

        lines.append(
            "## Recent Conversation"
        )

        lines.append("")

        for message in messages:

            lines.append(
                f"### {message.role}"
            )

            lines.append(
                message.content[:500]
            )

            lines.append("")

        return "\n".join(lines)