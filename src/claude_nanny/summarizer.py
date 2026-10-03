from claude_nanny.models import Message


def create_summary(messages: list[Message]) -> str:
    if not messages:
        return "No messages found"

    summary = []

    summary.append("=" * 60)
    summary.append("CLAUDE NANNY SUMMARY")
    summary.append("=" * 60)

    summary.append(f"Total messages: {len(messages)}")
    summary.append("")

    summary.append("Recent conversation:")
    summary.append("")

    for message in messages[-10:]:
        summary.append(f"[{message.role}]")
        summary.append(message.content)
        summary.append("-" * 50)

    return "\n".join(summary)