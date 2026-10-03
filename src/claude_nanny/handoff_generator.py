from claude_nanny.models import Message
from claude_nanny.gemini_client import GeminiClient


class HandoffGenerator:

    def __init__(self):
        self.gemini = GeminiClient()

    def generate(self, messages: list[Message]) -> str:

        transcript = "\n\n".join(
            f"[{message.role}]\n{message.content}"
            for message in messages[-20:]
        )

        prompt = f"""
You are a senior engineering handoff assistant.

Analyze this Claude Code session.

Return ONLY markdown.

Format:

# Session Handoff

## Current Feature

## Completed

## In Progress

## Backend Requirements

## Files Mentioned

## Next Steps

Transcript:

{transcript}
"""

        return self.gemini.generate(prompt)