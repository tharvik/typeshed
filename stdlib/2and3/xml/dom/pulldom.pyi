# Stubs for xml.dom.pulldom

# TODO py2 very badly documented

from typing import IO, Iterable, Iterator, Optional, Tuple, Union
import xml.dom.minidom
import xml.sax
import xml.sax.handler
from xml.sax.xmlreader import XMLReader

_Node = Union[
    xml.dom.minidom.Document,
    xml.dom.minidom.Element,
    xml.dom.minidom.Text,
]


START_ELEMENT = ...  # type: str
END_ELEMENT = ...  # type: str
COMMENT = ...  # type: str
START_DOCUMENT = ...  # type: str
END_DOCUMENT = ...  # type: str
CHARACTERS = ...  # type: str
PROCESSING_INSTRUCTION = ...  # type: str
IGNORABLE_WHITESPACE = ...  # type: str

class PullDOM(xml.sax.handler.ContentHandler): ...
class SAX2DOM(xml.sax.handler.ContentHandler): ...

def parse(stream_or_string: Union[str, IO[str]],
          parser: Optional[XMLReader] = ...,
          bufsize: Optional[int] = ...) -> DOMEventStream: ...
def parseString(string: str,
                parser: Optional[XMLReader] = ...) -> DOMEventStream: ...
default_bufsize = ...  # type: int


class DOMEventStream(Iterable[Tuple[int, _Node]]):
    def __init__(self, stream: int, parser: XMLReader,
                 bufsize: int) -> None: ...
    def getEvent(self) -> Tuple[int, _Node]: ...
    def expandNode(self, node: _Node) -> None: ...
    def reset(self) -> None: ...
    def __iter__(self) -> Iterator[Tuple[int, _Node]]: ...  # TODO undocumented
