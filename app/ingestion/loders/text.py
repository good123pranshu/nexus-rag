
from pathlib import Path

import logfire


def parse_text(file_path: str | Path) -> str:
    """
    Extract text content from a plain text file.

    Args:
        file_path: Path to the text file.

    Returns:
        Extracted text as a string.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the path is not a valid text file.
        UnicodeDecodeError: If the file cannot be decoded as UTF-8.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Text file not found: {path}")

    if not path.is_file():
        raise ValueError(f"Expected a file, got: {path}")

    if path.suffix.lower() != ".txt":
        raise ValueError(f"Expected a .txt file, got: {path.suffix}")

    with logfire.span("Text Parsing", filename=path.name):

        text_content = path.read_text(encoding="utf-8")

        return text_content.strip()
