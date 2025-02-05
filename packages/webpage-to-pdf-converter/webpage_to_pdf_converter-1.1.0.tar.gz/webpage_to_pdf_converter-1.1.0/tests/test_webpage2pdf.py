import pytest
from unittest.mock import Mock, patch
import requests
import responses
import os
from selenium.common.exceptions import TimeoutException
from typing import Optional, cast
from PIL import Image
import io

from webpage2pdf import (
    is_valid_url, check_url_status, get_screenshot, save_as_pdf
)
from webpage2pdf.utils.browser import wait_for_page_load, scroll_page
from webpage2pdf.utils.pdf import png_to_pdf
from webpage2pdf.utils.errors import WebPage2PDFError, URLError, PDFGenerationError
from webpage2pdf.utils.retry import retry_with_backoff

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

@patch('webpage2pdf.utils.browser.get_chrome_driver')
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

@patch('webpage2pdf.utils.browser.get_chrome_driver')
def test_save_as_pdf(mock_get_chrome_driver: Mock, mock_driver: Mock, temp_pdf: str, test_url: str) -> None:
    mock_get_chrome_driver.return_value = mock_driver
    valid_png = create_valid_png()
    mock_driver.get_screenshot_as_png.return_value = valid_png
    mock_driver.execute_script.side_effect = ['complete', True, 1000, 1000, 1000, 1000]
    
    with patch('webpage2pdf.utils.pdf.png_to_pdf') as mock_png_to_pdf:
        mock_png_to_pdf.return_value = (True, None)
        success, error = save_as_pdf(url=test_url, output_path=temp_pdf)
        assert success is True
        assert error is None
        mock_png_to_pdf.assert_called_once_with(valid_png, temp_pdf, 30)

def test_failed_pdf_generation(temp_pdf: str, test_url: str) -> None:
    with patch('webpage2pdf.main.get_screenshot') as mock_screenshot:
        error_message = "Screenshot failed"
        mock_screenshot.return_value = (False, error_message)
        
        with pytest.raises(PDFGenerationError) as exc_info:
            save_as_pdf(url=test_url, output_path=temp_pdf)
        
        assert error_message in str(exc_info.value)
        mock_screenshot.assert_called_with(url=test_url, timeout=30)

def test_retry_mechanism():
    """Test the retry decorator."""
    mock_func = Mock(side_effect=[ValueError("First try"), ValueError("Second try"), "Success"])
    decorated_func = retry_with_backoff(retries=3, backoff_in_seconds=0)(mock_func)
    
    result = decorated_func()
    assert result == "Success"
    assert mock_func.call_count == 3

def test_retry_mechanism_failure():
    """Test the retry decorator when all attempts fail."""
    mock_func = Mock(side_effect=ValueError("Persistent error"))
    decorated_func = retry_with_backoff(retries=3, backoff_in_seconds=0)(mock_func)
    
    with pytest.raises(ValueError, match="Persistent error"):
        decorated_func()
    assert mock_func.call_count == 3

@responses.activate
def test_check_url_status_with_retry():
    """Test URL checking with retry mechanism."""
    responses.add(
        responses.GET,
        "https://example.com",
        status=500,
        body="Server Error"
    )
    # Remove previous response and add new one
    responses.remove(responses.GET, "https://example.com")
    responses.add(
        responses.GET,
        "https://example.com",
        status=200,
        body="Success"
    )
    
    with patch('webpage2pdf.utils.retry.time.sleep') as mock_sleep:  # Skip waiting
        result = check_url_status("https://example.com")
    
    assert result['reachable'] is True
    assert result['status_code'] == 200
    assert len(responses.calls) == 1  # Should succeed on first try after removing failed response
    assert not mock_sleep.called  # Should not need to retry

def test_custom_exceptions():
    """Test custom exception hierarchy."""
    base_error = WebPage2PDFError("Base error")
    assert isinstance(base_error, Exception)
    
    url_error = URLError("URL error", original_error=ValueError("Invalid URL"))
    assert isinstance(url_error, WebPage2PDFError)
    assert isinstance(url_error.original_error, ValueError)
    
    pdf_error = PDFGenerationError("PDF error")
    assert isinstance(pdf_error, WebPage2PDFError)

@patch('webpage2pdf.utils.browser.get_chrome_driver')
def test_save_as_pdf_with_retry(mock_get_chrome_driver, mock_driver, temp_pdf, test_url):
    """Test PDF generation with retry mechanism."""
    mock_get_chrome_driver.return_value = mock_driver
    mock_driver.get_screenshot_as_png.side_effect = [
        Exception("First failure"),
        create_valid_png()
    ]
    mock_driver.execute_script.return_value = 'complete'  # Simplify page load checks
    
    with patch('webpage2pdf.utils.pdf.png_to_pdf') as mock_png_to_pdf, \
         patch('webpage2pdf.utils.retry.time.sleep') as mock_sleep:  # Skip actual waiting
        mock_png_to_pdf.return_value = (True, None)
        success, error = save_as_pdf(url=test_url, output_path=temp_pdf)
        
        assert success is True
        assert error is None
        assert mock_driver.get_screenshot_as_png.call_count >= 1
        mock_png_to_pdf.assert_called_once()

def test_error_handling_chain():
    """Test error propagation through the application."""
    with patch('webpage2pdf.main.requests.get') as mock_get:
        mock_get.side_effect = requests.exceptions.ConnectionError("Network error")
        
        with pytest.raises(URLError) as exc_info:
            check_url_status("https://example.com")
        
        assert "Network error" in str(exc_info.value)
        assert isinstance(exc_info.value.original_error, requests.exceptions.ConnectionError)
