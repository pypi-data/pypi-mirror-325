from typing import Optional

class WebPage2PDFError(Exception):
    """Base exception for webpage2pdf."""
    def __init__(self, message: str, original_error: Optional[Exception] = None):
        super().__init__(message)
        self.original_error = original_error

class BrowserError(WebPage2PDFError):
    """Raised when browser-related operations fail."""
    pass

class PDFGenerationError(WebPage2PDFError):
    """Raised when PDF generation fails."""
    pass

class URLError(WebPage2PDFError):
    """Raised when URL-related operations fail."""
    pass
