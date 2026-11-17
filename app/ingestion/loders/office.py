
from pathlib import Path

import logfire
from unstructured.partition.auto import partition


def parse_office(file_path: str | Path) -> str:
    """
    Extract text content from Office documents and other
    supported document formats using Unstructured.

    Args:
        file_path: Path to the document.

    Returns:
        Extracted text as a single string.

    Raises:
        FileNotFoundError: If the document does not exist.
        ValueError: If the provided path is not a file.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    if not path.is_file():
        raise ValueError(f"Expected a file, got: {path}")

    with logfire.span(
        "Office Document Parsing",
        filename=path.name,
        extension=path.suffix.lower()
    ):

        # Extract structured document elements
        elements = partition(filename=str(path))

        # Extract and clean text from each element
        text_parts = [
            element.text.strip()
            for element in elements
            if element.text and element.text.strip()
        ]

        # Combine elements while preserving paragraph separation
        text_content = "\n\n".join(text_parts)

        return text_content
