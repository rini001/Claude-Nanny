from pathlib import Path


class FileWriter:

    def save_handoff(
        self,
        content: str,
        output_path: Path,
    ) -> None:

        output_path.write_text(
            content,
            encoding="utf-8",
        )