from claude_nanny.discovery import SessionDiscovery


discovery = SessionDiscovery()

projects = discovery.get_project_directories()

print(f"Projects found: {len(projects)}\n")

for project in projects:
    print(project.name)

latest_session = discovery.get_latest_session(
    projects[0]
)

print("\nLatest session:")
print(latest_session.name)