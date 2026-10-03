from claude_nanny.discovery import SessionDiscovery


discovery = SessionDiscovery()

project = discovery.get_latest_active_project()

print("Latest Project:")
print(project.name)

session = discovery.get_latest_session(project)

print("\nLatest Session:")
print(session.name)