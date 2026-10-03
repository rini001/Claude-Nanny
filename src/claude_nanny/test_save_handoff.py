from pathlib import Path

from claude_nanny.file_writer import FileWriter

writer = FileWriter()

writer.save_handoff(
    "# Test Handoff",
    Path("handoffs/test.md"),
)

print("Saved!")