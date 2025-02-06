import logging
import sys

from bs4 import BeautifulSoup, NavigableString, PageElement, Tag
from htmlmin import minify  # type: ignore

from .....lib import Result
from .....utils.bitvec import Lsb
from ....errors import Error, ErrorKind
from ....managers.bits.encoder import BitEncoder
from ....managers.event import EventEncoder
from ...bits.utils import CHARS


class HtmlFileResponse(EventEncoder[Lsb]):
    """HTML file response encoder for SHDP protocol.

    This class handles encoding of HTML files for transmission, including:
    - File name encoding
    - HTML content minification
    - Tag structure preservation
    - Attribute handling
    - Text content encoding

    Attributes:
        encoder (BitEncoder[Lsb]): Bit encoder for the response
        path (str): Path to the HTML file

    Example:
        >>> response = HtmlFileResponse("templates/page.html")
        >>> response.encode()
        >>> encoder = response.get_encoder()
    """

    def __init__(self, path: str):
        """Initialize HTML file response.

        Args:
            path: Path to the HTML file to encode
        """
        logging.debug(
            f"[\x1b[38;5;227mSHDP\x1b[0m] \x1b[38;5;205m0x0001\x1b[0m created ({path})"
        )

        self.encoder = BitEncoder[Lsb]()
        self.path = path

    def _append_text(self, node: PageElement, text: str) -> Result[None, Error]:
        """Append text content to the encoder.

        Handles text node encoding with special cases:
        - Ignores empty text (whitespace only)
        - Skips text without parent
        - Preserves text in <pre> tags

        Args:
            node: Parent tag containing the text
            text: Text content to encode

        Returns:
            Result[None, Error]: Ok(None) if text was encoded successfully
        """
        if text.strip() == "":
            return Result.Ok(None)

        if node.parent is None:
            return Result.Ok(None)

        parent = node.parent

        if parent.name == "pre":
            return Result.Ok(None)

        Result.hide()

        self.encoder.add_data(0, 10)
        self.encoder.add_data(len(text), 15)
        self.encoder.add_bytes(text.encode("utf-8"))

        return Result.reveal()

    def _append_fyve_text(self, text: str) -> Result[None, Error]:
        """Encode text using the CHARS mapping.

        Converts each character to its corresponding CHARS code.

        Args:
            text: Text to encode using CHARS mapping

        Returns:
            Result[None, Error]: Ok(None) if encoding succeeds,
                               Err if text is empty
        """
        if text.strip() == "":
            return Result.Err(Error.new(ErrorKind.BAD_REQUEST, "Text is empty"))

        chars = list(text)

        Result.hide()

        for char in chars:
            self.encoder.add_vec(CHARS[char])

        return Result.reveal()

    def _process_node(
        self, node: PageElement, open_elements: list[str]
    ) -> Result[None, Error]:
        """Process an HTML node recursively.

        Handles different node types:
        - Tag nodes: Processes name, attributes and children
        - Text nodes: Encodes text content
        Maintains stack of open elements for proper nesting.

        Args:
            node: HTML node to process
            open_elements: Stack of currently open element names

        Returns:
            Result[None, Error]: Ok(None) if node was processed successfully
        """
        Result.hide()

        if isinstance(node, Tag):
            element_name = node.name

            open_elements.append(element_name)

            self.encoder.add_data(16, 10)
            self._append_fyve_text(element_name)

            if len(node.attrs) > 0:
                self.encoder.add_data(17, 10)

                for attr_name, attr_value in node.attrs.items():
                    if type(attr_value) == list:
                        self._append_fyve_text(attr_name)
                        self._append_text(node, str(" ".join(attr_value)))
                    else:
                        self._append_fyve_text(attr_name)
                        self._append_text(node, str(attr_value))

            self.encoder.add_data(24, 10)

            for child in node.contents:
                self._process_node(child, open_elements)

            open_elements.pop()

            self.encoder.add_data(25, 10)

        elif isinstance(node, NavigableString):
            self._append_text(node, str(node))

        return Result.reveal()

    def encode(self) -> Result[None, Error]:
        """Encode the complete HTML file.

        Process includes:
        1. Encoding the filename
        2. Reading and minifying HTML content
        3. Parsing with BeautifulSoup
        4. Processing all nodes recursively

        Returns:
            Result[None, Error]: Ok(None) if encoding succeeds
        """
        if sys.platform == "win32":
            html_file_name = self.path.split("\\")[-1]
        else:
            html_file_name = self.path.split("/")[-1]

        Result.hide()

        self.encoder.add_bytes(html_file_name.encode("utf-8"))
        self.encoder.add_data(0, 8)

        with open(self.path, "r", encoding="utf-8") as file:
            html_content = file.read()

        minified_html = minify(
            html_content, remove_comments=True, remove_empty_space=False
        )
        document = BeautifulSoup(minified_html, "html.parser")

        open_elements: list[str] = []
        for node in document.contents:
            self._process_node(node, open_elements)

        return Result.reveal()

    def get_encoder(self) -> BitEncoder[Lsb]:
        return self.encoder

    def get_event(self) -> int:
        return 0x0001
