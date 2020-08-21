from slack_bolt.request.async_request import AsyncBoltRequest
from slack_bolt.response import BoltResponse


def _is_url_verification(req: AsyncBoltRequest) -> bool:
    return (
        req is not None
        and req.payload is not None
        and req.payload.get("type", None) == "url_verification"
    )


def _is_ssl_check(req: AsyncBoltRequest) -> bool:
    return (
        req is not None
        and req.payload is not None
        and req.payload.get("type", None) == "ssl_check"
    )


def _is_no_auth_required(req: AsyncBoltRequest) -> bool:
    return _is_url_verification(req) or _is_ssl_check(req)


def _build_error_response() -> BoltResponse:
    # show an ephemeral message to the end-user
    return BoltResponse(
        status=200, body=":x: Please install this app into the workspace :bow:",
    )
