
from pathlib import Path

import logfire
from pypdf import PdfReader


def parse_pdf(file_path: str | Path) -> str:
    """
    Extract text content from a PDF document.

    Args:
        file_path: Path to the PDF file.

    Returns:
        Extracted text with page separation.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file is invalid or contains no extractable text.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"PDF file not found: {path}")

    if not path.is_file():
        raise ValueError(f"Expected a file, got: {path}")

    if path.suffix.lower() != ".pdf":
        raise ValueError(f"Expected a PDF file, got: {path.suffix}")

    with logfire.span("PDF Parsing", filename=path.name):

        reader = PdfReader(str(path))

        if reader.is_encrypted:
            raise ValueError(f"Encrypted PDF cannot be parsed: {path.name}")

        page_contents = []

        for page_number, page in enumerate(reader.pages, start=1):

            page_text = page.extract_text()

            if page_text and page_text.strip():
                page_contents.append(
                    f"Page {page_number}\n{page_text.strip()}"
                )

        text_content = "\n\n".join(page_contents)

        return text_content
