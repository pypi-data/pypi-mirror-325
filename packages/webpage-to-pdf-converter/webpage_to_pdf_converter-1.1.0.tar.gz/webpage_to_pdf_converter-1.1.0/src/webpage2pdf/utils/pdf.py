from PIL import Image
import tempfile
import os
from typing import Tuple, Optional
import threading
from io import BytesIO

def png_to_pdf(png_data: bytes, output_path: str, timeout: int = 30) -> Tuple[bool, Optional[str]]:
    """Convert PNG data to PDF with timeout."""
    def conversion_thread(png_data: bytes, output_path: str, result: dict):
        try:
            # Convert directly from memory without temporary file
            image = Image.open(BytesIO(png_data))
            if image.mode != 'RGB':
                image = image.convert('RGB')
            image.save(output_path, 'PDF', resolution=100.0)
            result['success'] = True
        except Exception as e:
            result['success'] = False
            result['error'] = str(e)

    result = {'success': False, 'error': None}
    thread = threading.Thread(
        target=conversion_thread,
        args=(png_data, output_path, result)
    )
    thread.daemon = True
    thread.start()
    thread.join(timeout=timeout * 2)  # Increase the timeout

    if thread.is_alive():
        return False, "PDF generation timed out"
    
    return result['success'], result.get('error')
