from claude_nanny.gemini_client import (
    GeminiClient
)

client = GeminiClient()

response = client.generate(
    "Say hello from Claude Nanny"
)

print(response)