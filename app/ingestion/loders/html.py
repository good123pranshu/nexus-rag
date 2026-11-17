
from pathlib import Path

from bs4 import BeautifulSoup
import logfire


def parse_html(file_path: str) -> str:
    """
    Extract clean text content from an HTML file.

    Args:
        file_path: Path to the HTML file.

    Returns:
        Extracted text content.
    """
    path = Path(file_path)

    with logfire.span("HTML Parsing", filename=str(path)):
        html_content = path.read_text(encoding="utf-8")

        soup = BeautifulSoup(html_content, "html.parser")

        # Remove elements that don't contain useful document content
        for element in soup(["script", "style", "noscript","meta"]):
            element.decompose()

        text_content = soup.get_text(
            separator="\n",
            strip=True
        )

        return text_content
