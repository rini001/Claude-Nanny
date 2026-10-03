from dataclasses import dataclass


@dataclass
class Message:
    role: str
    content: str


@dataclass
class Session:
    session_id: str
    project_path: str
    git_branch: str
    messages: list[Message]