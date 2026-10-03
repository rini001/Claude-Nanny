from pathlib import Path


class SessionDiscovery:

    def get_projects_directory(self) -> Path:
        return Path.home() / ".claude" / "projects"

    def get_project_directories(self) -> list[Path]:
        projects_dir = self.get_projects_directory()

        return [
            item
            for item in projects_dir.iterdir()
            if item.is_dir()
        ]

    def get_latest_session(self, project_dir: Path) -> Path:
        session_files = list(project_dir.glob("*.jsonl"))

        if not session_files:
            raise ValueError(
                f"No session files found in {project_dir}"
            )

        return max(
            session_files,
            key=lambda file: file.stat().st_mtime
        )

    def get_latest_active_project(self) -> Path:
        projects = self.get_project_directories()

        latest_project = None
        latest_time = 0

        for project in projects:

            try:
                latest_session = self.get_latest_session(project)

                modified_time = (
                    latest_session.stat().st_mtime
                )

                if modified_time > latest_time:
                    latest_time = modified_time
                    latest_project = project

            except ValueError:
                continue

        if latest_project is None:
            raise ValueError(
                "No active projects found"
            )

        return latest_project