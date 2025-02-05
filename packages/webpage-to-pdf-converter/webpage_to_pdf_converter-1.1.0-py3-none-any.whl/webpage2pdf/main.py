import click
import requests
from urllib.parse import urlparse
from typing import Dict, Any, Tuple, Optional, Union, cast
from selenium import webdriver
import os
import logging
import warnings

from webpage2pdf.utils.errors import WebPage2PDFError, URLError, PDFGenerationError
from webpage2pdf.utils.retry import retry_with_backoff
from webpage2pdf.utils.browser import with_driver, wait_for_page_load, scroll_page

# Configure warnings
warnings.filterwarnings('ignore', category=RuntimeWarning, message='.*found in sys.modules.*')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def is_valid_url(url: str) -> bool:
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

@retry_with_backoff(retries=3, exceptions=(URLError,))
def check_url_status(url: str, timeout: int = 5) -> Dict[str, Any]:
    """Check if a URL is reachable with retry mechanism."""
    try:
        response = requests.get(url, timeout=timeout)
        return {
            'status_code': response.status_code,
            'reachable': response.ok,
            'reason': response.reason
        }
    except requests.RequestException as e:
        raise URLError(f"Failed to check URL: {str(e)}", original_error=e)

@with_driver
def get_screenshot(url: str, timeout: int = 30, driver: Optional[webdriver.Chrome] = None) -> Tuple[bool, Union[bytes, str]]:
    """
    Capture screenshot of a webpage.
    
    Args:
        url: URL to capture
        timeout: Timeout in seconds
        driver: Optional Chrome webdriver instance (injected by decorator)
        
    Returns:
        Tuple of (success, result)
        where result is either bytes (screenshot data) or str (error message)
    """
    if not driver:
        return False, "No WebDriver provided"
        
    try:
        driver.get(url)
        
        if not wait_for_page_load(driver, timeout):
            return False, "Page load timeout"
            
        total_height = scroll_page(driver)
        driver.set_window_size(1920, total_height)
        
        screenshot = driver.get_screenshot_as_png()
        return True, screenshot
    except Exception as e:
        return False, str(e)

@retry_with_backoff(retries=3, exceptions=(PDFGenerationError,))
def save_as_pdf(url: str, output_path: str, timeout: int = 30) -> Tuple[bool, Optional[str]]:
    """Save webpage as PDF with retry mechanism."""
    logger.info("Starting PDF generation process...")
    try:
        logger.info("Capturing webpage screenshot...")
        success, result = get_screenshot(url=url, timeout=timeout)
        if not success:
            raise PDFGenerationError(f"Failed to capture screenshot: {result}")
        
        if isinstance(result, bytes) and result.startswith(b'\x89PNG\r\n\x1a\n'):
            logger.info("Converting screenshot to PDF...")
            from .utils.pdf import png_to_pdf
            return png_to_pdf(result, output_path, timeout)
        raise PDFGenerationError(f"Invalid screenshot data")
    except PDFGenerationError:
        raise  # Re-raise PDFGenerationError without wrapping
    except Exception as e:
        raise PDFGenerationError(f"PDF generation failed: {str(e)}", original_error=e)

@click.command()
@click.argument('url')
@click.option('--timeout', '-t', default=30, help='Timeout in seconds')
@click.option('--save-pdf', '-p', is_flag=True, help='Save webpage as PDF')
@click.option('--output', '-o', default='webpage.pdf', help='Output PDF filename')
@click.option('--retry/--no-retry', default=True, help='Retry on failure')
def main(url: str, timeout: int, save_pdf: bool, output: str, retry: bool):
    """Check URL and save webpage as PDF with improved error handling."""
    try:
        if not is_valid_url(url):
            raise URLError(f"Invalid URL: {url}")

        logger.info(f"Checking URL: {url}")
        with click.progressbar(length=1, label=f'Checking URL: {url}') as bar:
            result = check_url_status(url)
            bar.update(1)
        
        if result['reachable']:
            click.secho("✓ URL is reachable", fg='green')
            click.echo(f"Status code: {result['status_code']}")
            click.echo(f"Status: {result['reason']}")
            
            if save_pdf:
                with click.progressbar(length=3, label='Generating PDF') as bar:
                    try:
                        bar.update(1)  # Starting
                        success, error = save_as_pdf(url, output, timeout)
                        bar.update(1)  # Screenshot captured
                        if success:
                            logger.info(f"PDF saved successfully: {output}")
                            bar.update(1)  # PDF generated
                            click.secho(f"\n✓ PDF saved successfully as '{output}'", fg='green')
                            abs_path = os.path.abspath(output)
                            click.secho(f"File location: {abs_path}", fg='blue')
                        else:
                            logger.error(f"Failed to save PDF: {error}")
                            click.secho(f"✗ Failed to save PDF: {error}", fg='red')
                    except PDFGenerationError as e:
                        logger.error(f"PDF generation failed: {str(e)}")
                        if hasattr(e, 'original_error'):
                            logger.debug(f"Original error: {str(e.original_error)}")
                        raise
        else:
            raise URLError(f"URL is not reachable: {result['reason']}")
            
    except WebPage2PDFError as e:
        logger.error(str(e))
        if hasattr(e, 'original_error'):
            logger.debug(f"Original error: {str(e.original_error)}")
        raise click.ClickException(str(e))

if __name__ == '__main__':
    main()
