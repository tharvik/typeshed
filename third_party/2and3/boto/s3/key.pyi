# Stubs for boto.s3.key (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Callable, Dict, Optional, Text

class Key:
    DefaultContentType = ...  # type: str
    RestoreBody = ...  # type: str
    BufferSize = ...  # type: Any
    base_user_settable_fields = ...  # type: Any
    base_fields = ...  # type: Any
    bucket = ...  # type: Any
    name = ...  # type: str
    metadata = ...  # type: Any
    cache_control = ...  # type: Any
    content_type = ...  # type: Any
    content_encoding = ...  # type: Any
    content_disposition = ...  # type: Any
    content_language = ...  # type: Any
    filename = ...  # type: Any
    etag = ...  # type: Any
    is_latest = ...  # type: bool
    last_modified = ...  # type: Any
    owner = ...  # type: Any
    path = ...  # type: Any
    resp = ...  # type: Any
    mode = ...  # type: Any
    size = ...  # type: Any
    version_id = ...  # type: Any
    source_version_id = ...  # type: Any
    delete_marker = ...  # type: bool
    encrypted = ...  # type: Any
    ongoing_restore = ...  # type: Any
    expiry_date = ...  # type: Any
    local_hashes = ...  # type: Any
    def __init__(self, bucket: Optional[Any] = ..., name: Optional[Any] = ...) -> None: ...
    def __iter__(self): ...
    @property
    def provider(self): ...
    key = ...  # type: Any
    md5 = ...  # type: Any
    base64md5 = ...  # type: Any
    storage_class = ...  # type: Any
    def get_md5_from_hexdigest(self, md5_hexdigest): ...
    def handle_encryption_headers(self, resp): ...
    def handle_version_headers(self, resp, force: bool = ...): ...
    def handle_restore_headers(self, response): ...
    def handle_addl_headers(self, headers): ...
    def open_read(self, headers: Optional[Dict[Text, Text]] = ..., query_args: str = ..., override_num_retries: Optional[Any] = ..., response_headers: Optional[Dict[Text, Text]] = ...): ...
    def open_write(self, headers: Optional[Dict[Text, Text]] = ..., override_num_retries: Optional[Any] = ...): ...
    def open(self, mode: str = ..., headers: Optional[Dict[Text, Text]] = ..., query_args: Optional[Any] = ..., override_num_retries: Optional[Any] = ...): ...
    closed = ...  # type: bool
    def close(self, fast: bool = ...): ...
    def next(self): ...
    __next__ = ...  # type: Any
    def read(self, size: int = ...): ...
    def change_storage_class(self, new_storage_class, dst_bucket: Optional[Any] = ..., validate_dst_bucket: bool = ...): ...
    def copy(self, dst_bucket, dst_key, metadata: Optional[Any] = ..., reduced_redundancy: bool = ..., preserve_acl: bool = ..., encrypt_key: bool = ..., validate_dst_bucket: bool = ...): ...
    def startElement(self, name, attrs, connection): ...
    def endElement(self, name, value, connection): ...
    def exists(self, headers: Optional[Dict[Text, Text]] = ...): ...
    def delete(self, headers: Optional[Dict[Text, Text]] = ...): ...
    def get_metadata(self, name): ...
    def set_metadata(self, name, value): ...
    def update_metadata(self, d): ...
    def set_acl(self, acl_str, headers: Optional[Dict[Text, Text]] = ...): ...
    def get_acl(self, headers: Optional[Dict[Text, Text]] = ...): ...
    def get_xml_acl(self, headers: Optional[Dict[Text, Text]] = ...): ...
    def set_xml_acl(self, acl_str, headers: Optional[Dict[Text, Text]] = ...): ...
    def set_canned_acl(self, acl_str, headers: Optional[Dict[Text, Text]] = ...): ...
    def get_redirect(self): ...
    def set_redirect(self, redirect_location, headers: Optional[Dict[Text, Text]] = ...): ...
    def make_public(self, headers: Optional[Dict[Text, Text]] = ...): ...
    def generate_url(self, expires_in, method: str = ..., headers: Optional[Dict[Text, Text]] = ..., query_auth: bool = ..., force_http: bool = ..., response_headers: Optional[Dict[Text, Text]] = ..., expires_in_absolute: bool = ..., version_id: Optional[Any] = ..., policy: Optional[Any] = ..., reduced_redundancy: bool = ..., encrypt_key: bool = ...): ...
    def send_file(self, fp, headers: Optional[Dict[Text, Text]] = ..., cb: Optional[Callable[[int, int], Any]] = ..., num_cb: int = ..., query_args: Optional[Any] = ..., chunked_transfer: bool = ..., size: Optional[Any] = ...): ...
    def should_retry(self, response, chunked_transfer: bool = ...): ...
    def compute_md5(self, fp, size: Optional[Any] = ...): ...
    def set_contents_from_stream(self, fp, headers: Optional[Dict[Text, Text]] = ..., replace: bool = ..., cb: Optional[Callable[[int, int], Any]] = ..., num_cb: int = ..., policy: Optional[Any] = ..., reduced_redundancy: bool = ..., query_args: Optional[Any] = ..., size: Optional[Any] = ...): ...
    def set_contents_from_file(self, fp, headers: Optional[Dict[Text, Text]] = ..., replace: bool = ..., cb: Optional[Callable[[int, int], Any]] = ..., num_cb: int = ..., policy: Optional[Any] = ..., md5: Optional[Any] = ..., reduced_redundancy: bool = ..., query_args: Optional[Any] = ..., encrypt_key: bool = ..., size: Optional[Any] = ..., rewind: bool = ...): ...
    def set_contents_from_filename(self, filename, headers: Optional[Dict[Text, Text]] = ..., replace: bool = ..., cb: Optional[Callable[[int, int], Any]] = ..., num_cb: int = ..., policy: Optional[Any] = ..., md5: Optional[Any] = ..., reduced_redundancy: bool = ..., encrypt_key: bool = ...): ...
    def set_contents_from_string(self, string_data: Text, headers: Optional[Dict[Text, Text]] = ..., replace: bool = ..., cb: Optional[Callable[[int, int], Any]] = ..., num_cb: int = ..., policy: Optional[Any] = ..., md5: Optional[Any] = ..., reduced_redundancy: bool = ..., encrypt_key: bool = ...) -> None: ...
    def get_file(self, fp, headers: Optional[Dict[Text, Text]] = ..., cb: Optional[Callable[[int, int], Any]] = ..., num_cb: int = ..., torrent: bool = ..., version_id: Optional[Any] = ..., override_num_retries: Optional[Any] = ..., response_headers: Optional[Dict[Text, Text]] = ...): ...
    def get_torrent_file(self, fp, headers: Optional[Dict[Text, Text]] = ..., cb: Optional[Callable[[int, int], Any]] = ..., num_cb: int = ...): ...
    def get_contents_to_file(self, fp, headers: Optional[Dict[Text, Text]] = ..., cb: Optional[Callable[[int, int], Any]] = ..., num_cb: int = ..., torrent: bool = ..., version_id: Optional[Any] = ..., res_download_handler: Optional[Any] = ..., response_headers: Optional[Dict[Text, Text]] = ...): ...
    def get_contents_to_filename(self, filename, headers: Optional[Dict[Text, Text]] = ..., cb: Optional[Callable[[int, int], Any]] = ..., num_cb: int = ..., torrent: bool = ..., version_id: Optional[Any] = ..., res_download_handler: Optional[Any] = ..., response_headers: Optional[Dict[Text, Text]] = ...): ...
    def get_contents_as_string(self, headers: Optional[Dict[Text, Text]] = ..., cb: Optional[Callable[[int, int], Any]] = ..., num_cb: int = ..., torrent: bool = ..., version_id: Optional[Any] = ..., response_headers: Optional[Dict[Text, Text]] = ..., encoding: Optional[Any] = ...) -> str: ...
    def add_email_grant(self, permission, email_address, headers: Optional[Dict[Text, Text]] = ...): ...
    def add_user_grant(self, permission, user_id, headers: Optional[Dict[Text, Text]] = ..., display_name: Optional[Any] = ...): ...
    def set_remote_metadata(self, metadata_plus, metadata_minus, preserve_acl, headers: Optional[Dict[Text, Text]] = ...): ...
    def restore(self, days, headers: Optional[Dict[Text, Text]] = ...): ...