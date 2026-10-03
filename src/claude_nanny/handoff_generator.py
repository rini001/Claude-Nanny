from claude_nanny.models import Message
from claude_nanny.gemini_client import (
    GeminiClient,
)


class HandoffGenerator:

    def __init__(self):
        self.gemini = GeminiClient()

    def generate(
        self,
        messages: list[Message],
    ) -> str:

        transcript_parts = []

        for message in messages:

            transcript_parts.append(
                f"[{message.role}]\n"
                f"{message.content}"
            )

        transcript = "\n\n".join(
            transcript_parts
        )

        prompt = f"""
You are a senior engineering handoff assistant.

Analyze ALL work completed today.

Return ONLY markdown.

Format:

# Daily Engineering Handoff

## Features Worked On

## Completed

## In Progress

## Decisions Made

## Backend Requirements

## Files Mentioned

## Blockers

## Next Steps

Transcript:

{transcript}
"""

        return self.gemini.generate(
            prompt
        )