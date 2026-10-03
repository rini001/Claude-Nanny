from claude_nanny.discovery import SessionDiscovery
from claude_nanny.reader import SessionReader
from claude_nanny.handoff_generator import HandoffGenerator

discovery = SessionDiscovery()

project = discovery.get_latest_active_project()
session = discovery.get_latest_session(project)

reader = SessionReader()
messages = reader.read_messages(session)

generator = HandoffGenerator()

handoff = generator.generate(messages)

print(handoff)