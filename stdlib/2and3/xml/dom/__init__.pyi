# Stubs for xml.dom

from typing import Callable, Optional, Sequence, Sized, Tuple
from abc import abstractmethod


def registerDOMImplementation(name: str,
                              factory: Callable[[], DomImplementation]) -> None: ...
def getDOMImplementation(name: Optional[str] = ...,
                         features: Sequence[Tuple[str, str]] = ...) -> DomImplementation: ...
EMPTY_NAMESPACE = ...  # type: None
XML_NAMESPACE = ...  # type: str
XMLNS_NAMESPACE = ...  # type: str
XHTML_NAMESPACE = ...  # type: str


class DomImplementation:
    @abstractmethod
    def hasFeature(self, feature: str, version: str) -> bool: ...
    @abstractmethod
    def createDocument(self, namespaceUri: Optional[str],
                       qualifiedName: Optional[str],
                       doctype: Optional[str]) -> Document: ...
    @abstractmethod
    def createDocumentType(self, qualifiedName: str, publicId: str,
                           systemId: str) -> DocumentType: ...


class Node:
    @property
    @abstractmethod
    def nodeType(self) -> int: ...
    ELEMENT_NODE = ...  # type: int
    ATTRIBUTE_NODE = ...  # type: int
    TEXT_NODE = ...  # type: int
    CDATA_SECTION_NODE = ...  # type: int
    ENTITY_NODE = ...  # type: int
    PROCESSING_INSTRUCTION_NODE = ...  # type: int
    COMMENT_NODE = ...  # type: int
    DOCUMENT_NODE = ...  # type: int
    DOCUMENT_TYPE_NODE = ...  # type: int
    NOTATION_NODE = ...  # type: int
    @property
    @abstractmethod
    def parentNode(self) -> Optional[Node]: ...
    @property
    @abstractmethod
    def attributes(self) -> Optional[NamedNodeMap]: ...
    @property
    @abstractmethod
    def previousSibling(self) -> Optional[Node]: ...
    @property
    @abstractmethod
    def nextSibling(self) -> Optional[Node]: ...
    @property
    @abstractmethod
    def childNodes(self) -> List[Node]: ...
    @property
    @abstractmethod
    def firstChild(self) -> Optional[Node]: ...
    @property
    @abstractmethod
    def lastChild(self) -> Optional[Node]: ...
    @property
    @abstractmethod
    def localName(self) -> str: ...
    @property
    @abstractmethod
    def prefix(self) -> Optional[str]: ...
    @property
    @abstractmethod
    def namespaceURI(self) -> Optional[str]: ...
    @property
    @abstractmethod
    def nodeName(self) -> Optional[str]: ...
    @property
    @abstractmethod
    def nodeValue(self) -> Optional[str]: ...
    @abstractmethod
    def hasAttributes(self) -> bool: ...
    @abstractmethod
    def hasChildNodes(self) -> bool: ...
    @abstractmethod
    def isSameNode(self, other: Node) -> bool: ...
    @abstractmethod
    def appendChild(self, newChild: Node) -> None: ...
    @abstractmethod
    def insertBefore(self, newChild: Node, refChild: Optional[Node]) -> Node: ...
    @abstractmethod
    def removeChild(self, oldChild: Node) -> Node: ...
    @abstractmethod
    def replaceChild(self, newChild: Node, oldChild: Node) -> None: ...
    @abstractmethod
    def normalize(self) -> None: ...
    @abstractmethod
    def cloneNode(self, deep: bool) -> Node: ...


class NodeList(Sized):
    @property
    @abstractmethod
    def length(self) -> int: ...
    @abstractmethod
    def item(self, i: int) -> Optional[Node]: ...
    @abstractmethod
    def __getitem__(self, i: int) -> Optional[Node]: ...


class DocumentType(Node):
    @property
    @abstractmethod
    def publicId(self) -> Optional[str]: ...
    @property
    @abstractmethod
    def systemId(self) -> Optional[str]: ...
    @property
    @abstractmethod
    def internalSubset(self) -> Optional[str]: ...
    @property
    @abstractmethod
    def name(self) -> str: ...
    @property
    @abstractmethod
    def entities(self) -> Optional[NamedNodeMap]: ...
    @property
    @abstractmethod
    def notations(self) -> Optional[NamedNodeMap]: ...


class Document(Node):
    @property
    @abstractmethod
    def documentElement(self) -> Element: ...
    @abstractmethod
    def createElement(self, tagName: str) -> Element: ...
    @abstractmethod
    def createElementNS(self, namespaceURI: str, tagName: str) -> Element: ...
    @abstractmethod
    def createTextNode(self, data: str) -> Text: ...
    @abstractmethod
    def createComment(self, data: str) -> Comment: ...
    @abstractmethod
    def createProcessingInstruction(self, target: str,
                                    data: str) -> ProcessingInstruction: ...
    @abstractmethod
    def createAttribute(self, name: str) -> Attr: ...
    @abstractmethod
    def createAttributeNS(self, namespaceURI: str,
                          qualifiedName: str) -> Attr: ...
    @abstractmethod
    def getElementsByTagName(self, tagName: str) -> NodeList: ...
    @abstractmethod
    def getElementsByTagNameNS(self, namespaceURI: str,
                               localName: str) -> NodeList: ...


class Element(Node):
    @property
    @abstractmethod
    def tagName(self) -> str: ...
    @abstractmethod
    def getElementsByTagName(self, tagName: str) -> NodeList: ...
    @abstractmethod
    def getElementsByTagNameNS(self, namespaceURI: str,
                               localName: str) -> NodeList: ...
    @abstractmethod
    def hasAttribute(self, name: str) -> bool: ...
    @abstractmethod
    def hasAttributeNS(self, namespaceURI: str, localName: str) -> bool: ...
    @abstractmethod
    def getAttribute(self, name: str) -> str: ...
    @abstractmethod
    def getAttributeNode(self, attrname: str) -> Attr: ...
    @abstractmethod
    def getAttributeNS(self, namespaceURI: str, localName: str) -> str: ...
    @abstractmethod
    def getAttributeNodeNS(self, namespaceURI: str, localName: str) -> Attr: ...
    @abstractmethod
    def removeAttribute(self, name: str) -> None: ...
    @abstractmethod
    def removeAttributeNode(self, oldAttr: Attr) -> None: ...
    @abstractmethod
    def removeAttributeNS(self, namespaceURI: str, localName: str) -> None: ...
    @abstractmethod
    def setAttribute(self, name: str, value: str) -> None: ...
    @abstractmethod
    def setAttributeNode(self, newAttr: Attr) -> Node: ...
    @abstractmethod
    def setAttributeNodeNS(self, newAttr: Attr) -> Node: ...
    @abstractmethod
    def setAttributeNS(self, namespaceURI: str, qname: str,
                       value: Attr) -> None: ...


class Attr(Node):
    @property
    @abstractmethod
    def name(self) -> str: ...
    @property
    @abstractmethod
    def prefix(self) -> str: ...
    @property
    @abstractmethod
    def value(self) -> Optional[str]: ...


class NamedNodeMap:
    @property
    @abstractmethod
    def length(self) -> int: ...
    @abstractmethod
    def item(self, index: int) -> Attr: ...


class Comment(Node):
    @property
    @abstractmethod
    def data(self) -> str: ...


class Text(Node):
    @property
    @abstractmethod
    def data(self) -> str: ...


class ProcessingInstruction(Node):
    @property
    @abstractmethod
    def target(self) -> str: ...
    @property
    @abstractmethod
    def data(self) -> str: ...


class DOMException(Exception):
    @property
    @abstractmethod
    def code(self) -> int: ...

class DomstringSizeErr(DOMException):
    @property
    def code(self) -> int: ...

class HierarchyRequestErr(DOMException):
    @property
    def code(self) -> int: ...

class IndexSizeErr(DOMException):
    @property
    def code(self) -> int: ...

class InuseAttributeErr(DOMException):
    @property
    def code(self) -> int: ...

class InvalidAccessErr(DOMException):
    @property
    def code(self) -> int: ...

class InvalidCharacterErr(DOMException):
    @property
    def code(self) -> int: ...

class InvalidModificationErr(DOMException):
    @property
    def code(self) -> int: ...

class InvalidStateErr(DOMException):
    @property
    def code(self) -> int: ...

class NamespaceErr(DOMException):
    @property
    def code(self) -> int: ...

class NotFoundErr(DOMException):
    @property
    def code(self) -> int: ...

class NotSupportedErr(DOMException):
    @property
    def code(self) -> int: ...

class NoDataAllowedErr(DOMException):
    @property
    def code(self) -> int: ...

class NoModificationAllowedErr(DOMException):
    @property
    def code(self) -> int: ...

class SyntaxErr(DOMException):
    @property
    def code(self) -> int: ...

class WrongDocumentErr(DOMException):
    @property
    def code(self) -> int: ...

DOMSTRING_SIZE_ERR = ...  # type: int
HIERARCHY_REQUEST_ERR = ...  # type: int
INDEX_SIZE_ERR = ...  # type: int
INUSE_ATTRIBUTE_ERR = ...  # type: int
INVALID_ACCESS_ERR = ...  # type: int
INVALID_CHARACTER_ERR = ...  # type: int
INVALID_MODIFICATION_ERR = ...  # type: int
INVALID_STATE_ERR = ...  # type: int
NAMESPACE_ERR = ...  # type: int
NOT_FOUND_ERR = ...  # type: int
NOT_SUPPORTED_ERR = ...  # type: int
NO_DATA_ALLOWED_ERR = ...  # type: int
NO_MODIFICATION_ALLOWED_ERR = ...  # type: int
SYNTAX_ERR = ...  # type: int
WRONG_DOCUMENT_ERR = ...  # type: int
