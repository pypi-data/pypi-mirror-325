from typing import Optional
from core_infinity_stones.errors.base_error import BaseError


class ResponseStatusCodeError(BaseError):
    def __init__(
        self,
        url: str,
        status_code: int,
        occurred_while: str,
        debug_description: str,
        messages_by_status_codes: Optional[dict[int, str]] = None,
    ):
        error_message = (
            messages_by_status_codes.get(status_code)
            if messages_by_status_codes
            else None
        )

        super().__init__(
            status_code=status_code,
            occurred_while=occurred_while,
            debug_description=f"url: {url}, error: {debug_description}",
            message=error_message,
        )
