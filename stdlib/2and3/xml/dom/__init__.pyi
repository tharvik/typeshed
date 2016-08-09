# Stubs for xml.dom

from typing import Callable, Optional, Sequence, Sized, Tuple


def registerDOMImplementation(name: str,
                              factory: Callable[[], DomImplementation]) -> None: ...
def getDOMImplementation(name: Optional[str] = ...,
                         features: Sequence[Tuple[str, str]] = ...) -> DomImplementation: ...
EMPTY_NAMESPACE = ...  # type: None
XML_NAMESPACE = ...  # type: str
XMLNS_NAMESPACE = ...  # type: str
XHTML_NAMESPACE = ...  # type: str


class DomImplementation:
    def hasFeature(self, feature: str, version: str) -> bool: ...
    def createDocument(self, namespaceUri: Optional[str],
                       qualifiedName: Optional[str],
                       doctype: Optional[str]) -> Document: ...
    def createDocumentType(self, qualifiedName: str, publicId: str,
                           systemId: str) -> DocumentType: ...


class Node:
    @property
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
    def parentNode(self) -> Optional[Node]: ...
    @property
    def attributes(self) -> Optional[NamedNodeMap]: ...
    @property
    def previousSibling(self) -> Optional[Node]: ...
    @property
    def nextSibling(self) -> Optional[Node]: ...
    @property
    def childNodes(self) -> List[Node]: ...
    @property
    def firstChild(self) -> Optional[Node]: ...
    @property
    def lastChild(self) -> Optional[Node]: ...
    localName = ...  # type: str
    prefix = ...  # type: Optional[str]
    @property
    def namespaceURI(self) -> Optional[str]: ...
    @property
    def nodeName(self) -> Optional[str]: ...
    nodeValue = ...  # type: Optional[str]
    def hasAttributes(self) -> bool: ...
    def hasChildNodes(self) -> bool: ...
    def isSameNode(self, other: Node) -> bool: ...
    def appendChild(self, newChild: Node) -> None: ...
    def insertBefore(self, newChild: Node, refChild: Optional[Node]) -> Node: ...
    def removeChild(self, oldChild: Node) -> Node: ...
    def replaceChild(self, newChild: Node, oldChild: Node) -> None: ...
    def normalize(self) -> None: ...
    def cloneNode(self, deep: bool) -> Node: ...


class NodeList(Sized):
    length = ...  # type: int
    def item(self, i: int) -> Optional[Node]: ...
    def __getitem__(self, i: int) -> Optional[Node]: ...


class DocumentType(Node):
    publicId = ...  # type: Optional[str]
    systemId = ...  # type: Optional[str]
    internalSubset = ...  # type: Optional[str]
    name = ...  # type: str
    entities = ...  # type: Optional[NamedNodeMap]
    notations = ...  # type: Optional[NamedNodeMap]


class Document(Node):
    documentElement = ...  # type: Element
    def createElement(self, tagName: str) -> Element: ...
    def createElementNS(self, namespaceURI: str, tagName: str) -> Element: ...
    def createTextNode(self, data: str) -> Text: ...
    def createComment(self, data: str) -> Comment: ...
    def createProcessingInstruction(self, target: str,
                                    data: str) -> ProcessingInstruction: ...
    def createAttribute(self, name: str) -> Attr: ...
    def createAttributeNS(self, namespaceURI: str,
                          qualifiedName: str) -> Attr: ...
    def getElementsByTagName(self, tagName: str) -> NodeList: ...
    def getElementsByTagNameNS(self, namespaceURI: str,
            localName: str) -> NodeList: ...


class Element(Node):
    tagName = ...  # type: str
    def getElementsByTagName(self, tagName: str) -> NodeList: ...
    def getElementsByTagNameNS(self, namespaceURI: str,
            localName: str) -> NodeList: ...
    def hasAttribute(self, name: str) -> bool: ...
    def hasAttributeNS(self, namespaceURI: str, localName: str) -> bool: ...
    def getAttribute(self, name: str) -> str: ...
    def getAttributeNode(self, attrname: str) -> Attr: ...
    def getAttributeNS(self, namespaceURI: str, localName: str) -> str: ...
    def getAttributeNodeNS(self, namespaceURI: str, localName: str) -> Attr: ...
    def removeAttribute(self, name: str) -> None: ...
    def removeAttributeNode(self, oldAttr: Attr) -> None: ...
    def removeAttributeNS(self, namespaceURI: str, localName: str) -> None: ...
    def setAttribute(self, name: str, value: str) -> None: ...
    def setAttributeNode(self, newAttr: Attr) -> Node: ...
    def setAttributeNodeNS(self, newAttr: Attr) -> Node: ...
    def setAttributeNS(self, namespaceURI: str, qname: str,
                       value: Attr) -> None: ...


class Attr(Node):
    name = ...  # type: str
    @property
    def localName(self) -> str: ...  # type: ignore
    prefix = ...  # type: str
    value = ...  # type: Optional[str]


class NamedNodeMap:
    length = ...  # type: int
    def item(self, index: int) -> Attr: ...


class Comment(Node):
    data = ...  # type: str


class Text(Node):
    data = ...  # type: str


class ProcessingInstruction(Node):
    @property
    def target(self) -> str: ...
    data = ...  # type: str


class DOMException(Exception):
    @property
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


#class UserDataHandler:
#    NODE_CLONED = ...  # type: Any
#    NODE_IMPORTED = ...  # type: Any
#    NODE_DELETED = ...  # type: Any
#    NODE_RENAMED = ...  # type: Any

#EMPTY_PREFIX = ...  # type: Any

