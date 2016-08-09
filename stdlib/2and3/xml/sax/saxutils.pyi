# Stubs for xml.sax.saxutils

from typing import IO, Mapping, Optional, Union
from xml.sax.handler import ContentHandler
from xml.sax.xmlreader import XMLReader, InputSource
import sys

def escape(data: str, entities: Mapping[str, str] = ...) -> str: ...
def unescape(data: str, entities: Mapping[str, str] = ...) -> str: ...
def quoteattr(data: str, entities: Mapping[str, str] = ...) -> str: ...

class XMLGenerator(ContentHandler):
    if sys.version_info >= (3,):
        def __init__(self, out: Optional[IO[str]] = ..., encoding: str = ...,
                     short_empty_elements: bool = ...) -> None: ...
    else:
        def __init__(self, out: Optional[IO[str]] = ...,
                     encoding: str = ...) -> None: ...

class XMLFilterBase(XMLReader):
    def __init__(self, base: XMLReader) -> None: ...

def prepare_input_source(source: Union[str, IO[str], InputSource],
                         base: str = ...) -> InputSource: ...
