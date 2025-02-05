import pytest
from unittest.mock import Mock, patch
import responses
import os
from selenium.common.exceptions import TimeoutException
from typing import Optional, cast
from PIL import Image
import io

from src.webpage2pdf import (
    is_valid_url, check_url_status, get_screenshot, save_as_pdf
)
from src.webpage2pdf.utils.browser import wait_for_page_load, scroll_page
from src.webpage2pdf.utils.pdf import png_to_pdf

def create_valid_png():
    img = Image.new("RGB", (100, 100), color="blue")
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()

def test_is_valid_url(test_url, invalid_url):
    assert is_valid_url(test_url) is True
    assert is_valid_url(invalid_url) is False

@responses.activate
def test_check_url_status(test_url):
    # Mock successful response
    responses.add(
        responses.GET,
        test_url,
        status=200,
        body="OK"
    )
    result = check_url_status(test_url)
    assert result['reachable'] is True
    assert result['status_code'] == 200

    # Mock failed response
    responses.add(
        responses.GET,
        "https://nonexistent.example.com",
        status=404
    )
    result = check_url_status("https://nonexistent.example.com")
    assert result['reachable'] is False
    assert result['status_code'] == 404

def test_wait_for_page_load(mock_driver):
    mock_driver.execute_script.side_effect = [
        'complete',
        True,
    ]
    assert wait_for_page_load(mock_driver, timeout=1) is True

    mock_driver.execute_script.side_effect = TimeoutException("Timeout")
    assert wait_for_page_load(mock_driver, timeout=1) is False

@patch('src.webpage2pdf.utils.browser.get_chrome_driver')
def test_screenshot_capture(mock_get_chrome_driver: Mock, mock_driver: Mock, test_url: str) -> None:
    mock_get_chrome_driver.return_value = mock_driver
    valid_png = create_valid_png()
    mock_driver.get_screenshot_as_png.return_value = valid_png
    mock_driver.execute_script.side_effect = ['complete', True, 1000, 1000, 1000, 1000]
    
    success, data = get_screenshot(url=test_url)
    
    assert success is True
    assert isinstance(data, bytes)
    assert data.startswith(b'\x89PNG\r\n\x1a\n')
    mock_driver.get.assert_called_once_with(test_url)
    assert mock_driver.execute_script.call_count == 6

@patch('src.webpage2pdf.utils.browser.get_chrome_driver')
def test_save_as_pdf(mock_get_chrome_driver: Mock, mock_driver: Mock, temp_pdf: str, test_url: str) -> None:
    mock_get_chrome_driver.return_value = mock_driver
    valid_png = create_valid_png()
    mock_driver.get_screenshot_as_png.return_value = valid_png
    mock_driver.execute_script.side_effect = ['complete', True, 1000, 1000, 1000, 1000]
    
    with patch('src.webpage2pdf.utils.pdf.png_to_pdf') as mock_png_to_pdf:
        mock_png_to_pdf.return_value = (True, None)
        success, error = save_as_pdf(url=test_url, output_path=temp_pdf)
        assert success is True
        assert error is None
        mock_png_to_pdf.assert_called_once_with(valid_png, temp_pdf, 30)

def test_failed_pdf_generation(temp_pdf: str, test_url: str) -> None:
    with patch('src.webpage2pdf.main.get_screenshot') as mock_screenshot:
        error_message = "Screenshot failed"
        mock_screenshot.return_value = (False, error_message)
        
        success, error = save_as_pdf(url=test_url, output_path=temp_pdf)
        
        assert success is False
        assert error is not None
        assert isinstance(error, str)
        assert error_message in str(error)
        mock_screenshot.assert_called_once_with(url=test_url, timeout=30)
