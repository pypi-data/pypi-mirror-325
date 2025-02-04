import typing
import httpx


def remove_none_from_dict(
    original: typing.Dict[str, typing.Optional[typing.Any]],
) -> typing.Dict[str, typing.Any]:
    new: typing.Dict[str, typing.Any] = {}
    for key, value in original.items():
        if value is not None:
            new[key] = value
    return new


def is_binary_content_type(content_type: str) -> bool:
    """Check if the content type indicates binary data."""
    binary_types = [
        "application/octet-stream",
        "application/pdf",
        "application/zip",
        "image/",
        "audio/",
        "video/",
        "application/msword",
        "application/vnd.openxmlformats-officedocument",
        "application/x-binary",
        "application/vnd.ms-excel",
        "application/vnd.ms-powerpoint",
    ]
    return any(binary_type in content_type for binary_type in binary_types)


def get_content_type(headers: httpx.Headers) -> str:
    """Get content type in a case-insensitive manner."""
    for key, value in headers.items():
        if key.lower() == "content-type":
            return value.lower()
    return ""
