# Stubs for xml.dom

from typing import Callable, Optional, Sequence, Tuple
#from .domreg import getDOMImplementation as getDOMImplementation, registerDOMImplementation as registerDOMImplementation

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

#class Node:
#    ELEMENT_NODE = ...  # type: Any
#    ATTRIBUTE_NODE = ...  # type: Any
#    TEXT_NODE = ...  # type: Any
#    CDATA_SECTION_NODE = ...  # type: Any
#    ENTITY_REFERENCE_NODE = ...  # type: Any
#    ENTITY_NODE = ...  # type: Any
#    PROCESSING_INSTRUCTION_NODE = ...  # type: Any
#    COMMENT_NODE = ...  # type: Any
#    DOCUMENT_NODE = ...  # type: Any
#    DOCUMENT_TYPE_NODE = ...  # type: Any
#    DOCUMENT_FRAGMENT_NODE = ...  # type: Any
#    NOTATION_NODE = ...  # type: Any

#INDEX_SIZE_ERR = ...  # type: Any
#DOMSTRING_SIZE_ERR = ...  # type: Any
#HIERARCHY_REQUEST_ERR = ...  # type: Any
#WRONG_DOCUMENT_ERR = ...  # type: Any
#INVALID_CHARACTER_ERR = ...  # type: Any
#NO_DATA_ALLOWED_ERR = ...  # type: Any
#NO_MODIFICATION_ALLOWED_ERR = ...  # type: Any
#NOT_FOUND_ERR = ...  # type: Any
#NOT_SUPPORTED_ERR = ...  # type: Any
#INUSE_ATTRIBUTE_ERR = ...  # type: Any
#INVALID_STATE_ERR = ...  # type: Any
#SYNTAX_ERR = ...  # type: Any
#INVALID_MODIFICATION_ERR = ...  # type: Any
#NAMESPACE_ERR = ...  # type: Any
#INVALID_ACCESS_ERR = ...  # type: Any
#VALIDATION_ERR = ...  # type: Any

#class DOMException(Exception):
#    def __init__(self, *args, **kw): ...

#class IndexSizeErr(DOMException):
#    code = ...  # type: Any

#class DomstringSizeErr(DOMException):
#    code = ...  # type: Any

#class HierarchyRequestErr(DOMException):
#    code = ...  # type: Any

#class WrongDocumentErr(DOMException):
#    code = ...  # type: Any

#class InvalidCharacterErr(DOMException):
#    code = ...  # type: Any

#class NoDataAllowedErr(DOMException):
#    code = ...  # type: Any

#class NoModificationAllowedErr(DOMException):
#    code = ...  # type: Any

#class NotFoundErr(DOMException):
#    code = ...  # type: Any

#class NotSupportedErr(DOMException):
#    code = ...  # type: Any

#class InuseAttributeErr(DOMException):
#    code = ...  # type: Any

#class InvalidStateErr(DOMException):
#    code = ...  # type: Any

#class SyntaxErr(DOMException):
#    code = ...  # type: Any

#class InvalidModificationErr(DOMException):
#    code = ...  # type: Any

#class NamespaceErr(DOMException):
#    code = ...  # type: Any

#class InvalidAccessErr(DOMException):
#    code = ...  # type: Any

#class ValidationErr(DOMException):
#    code = ...  # type: Any

#class UserDataHandler:
#    NODE_CLONED = ...  # type: Any
#    NODE_IMPORTED = ...  # type: Any
#    NODE_DELETED = ...  # type: Any
#    NODE_RENAMED = ...  # type: Any

#EMPTY_PREFIX = ...  # type: Any

class Document: ...
class DocumentType: ...
