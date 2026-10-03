from pathlib import Path

project_dir = (
    Path.home()
    / ".claude"
    / "projects"
    / "c--Users-Dell-Desktop-New-folder--5--shiftninja-client"
)

session_files = list(project_dir.glob("*.jsonl"))

latest_session = max(
    session_files,
    key=lambda file: file.stat().st_mtime
)

print("Latest session:")
print(latest_session.name)
print()

print("Last modified:")
print(latest_session.stat().st_mtime)