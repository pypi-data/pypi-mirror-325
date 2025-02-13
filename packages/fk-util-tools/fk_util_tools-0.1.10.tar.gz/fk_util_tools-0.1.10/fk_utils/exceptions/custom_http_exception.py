from fastapi import HTTPException
from enum import Enum


class CustomHTTPException(HTTPException):
    def __init__(self, error_code: Enum, detail: str = None):
        super().__init__(status_code=error_code.status_code)
        self.error_code = error_code
        self.detail = detail or error_code.detail
