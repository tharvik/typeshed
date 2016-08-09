# Stubs for xml.sax.handler

from typing import List


class ContentHandler: ...
#    def __init__(self): ...
#    def setDocumentLocator(self, locator): ...
#    def startDocument(self): ...
#    def endDocument(self): ...
#    def startPrefixMapping(self, prefix, uri): ...
#    def endPrefixMapping(self, prefix): ...
#    def startElement(self, name, attrs): ...
#    def endElement(self, name): ...
#    def startElementNS(self, name, qname, attrs): ...
#    def endElementNS(self, name, qname): ...
#    def characters(self, content): ...
#    def ignorableWhitespace(self, whitespace): ...
#    def processingInstruction(self, target, data): ...
#    def skippedEntity(self, name): ...


class DTDHandler: ...
#    def notationDecl(self, name, publicId, systemId): ...
#    def unparsedEntityDecl(self, name, publicId, systemId, ndata): ...


class EntityResolver: ...
#    def resolveEntity(self, publicId, systemId): ...


class ErrorHandler: ...
#    def error(self, exception): ...
#    def fatalError(self, exception): ...
#    def warning(self, exception): ...


feature_namespaces = ...  # type: str
feature_namespace_prefixes = ...  # type: str
feature_string_interning = ...  # type: str
feature_validation = ...  # type: str
feature_external_ges = ...  # type: str
feature_external_pes = ...  # type: str
all_features = ...  # type: List[str]
property_lexical_handler = ...  # type: str
property_declaration_handler = ...  # type: str
property_dom_node = ...  # type: str
property_xml_string = ...  # type: str
all_properties = ...  # type: List[str]
