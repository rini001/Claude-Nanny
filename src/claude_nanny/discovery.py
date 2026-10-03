from pathlib import Path


def inspect_client_project():
    projects_dir = Path.home() / ".claude" / "projects"

    project_dir = (
        projects_dir
        / "c--Users-Dell-Desktop-New-folder--5--shiftninja-client"
    )

    print(f"Project: {project_dir}\n")

    if not project_dir.exists():
        print("Project not found")
        return

    items = list(project_dir.iterdir())

    print(f"Items found: {len(items)}\n")

    for item in items:
        item_type = "DIR" if item.is_dir() else "FILE"
        print(f"[{item_type}] {item.name}")


inspect_client_project()