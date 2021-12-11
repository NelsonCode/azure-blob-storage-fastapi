from typing import Iterable
from fastapi.responses import StreamingResponse


def response_stream(data: Iterable[bytes], status: int = 200, download: bool = False) -> StreamingResponse:
    if download:
        return StreamingResponse(content=data, status_code=status, media_type="application/octet-stream")
    else:
        return StreamingResponse(content=data, status_code=status)