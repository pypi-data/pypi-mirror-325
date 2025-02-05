import click
import requests
from urllib.parse import urlparse
from typing import Dict, Any, Tuple, Optional, Union, cast
from selenium import webdriver
import os

from .utils.browser import with_driver, wait_for_page_load, scroll_page

def is_valid_url(url: str) -> bool:
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def check_url_status(url: str, timeout: int = 5) -> Dict[str, Any]:
    try:
        response = requests.get(url, timeout=timeout)
        return {
            'status_code': response.status_code,
            'reachable': response.ok,
            'reason': response.reason
        }
    except requests.RequestException as e:
        return {
            'status_code': None,
            'reachable': False,
            'reason': str(e)
        }

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

def save_as_pdf(url: str, output_path: str, timeout: int = 30) -> Tuple[bool, Optional[str]]:
    success, result = get_screenshot(url=url, timeout=timeout)
    if not success:
        return False, f"Failed to capture screenshot: {result}"
    
    # Ensure result is bytes and starts with PNG header
    if isinstance(result, bytes) and result.startswith(b'\x89PNG\r\n\x1a\n'):
        from .utils.pdf import png_to_pdf  # Local import for patching
        return png_to_pdf(result, output_path, timeout)
    return False, f"Invalid screenshot data: {result}"

@click.command()
@click.argument('url')
@click.option('--timeout', '-t', default=30, help='Timeout in seconds')
@click.option('--save-pdf', '-p', is_flag=True, help='Save webpage as PDF')
@click.option('--output', '-o', default='webpage.pdf', help='Output PDF filename')
@click.option('--retry/--no-retry', default=True, help='Retry on failure')
def main(url: str, timeout: int, save_pdf: bool, output: str, retry: bool):
    """Check if a URL is reachable and optionally save as PDF."""
    if not is_valid_url(url):
        click.secho(f"Error: '{url}' is not a valid URL", fg='red')
        return

    with click.progressbar(length=1, label=f'Checking URL: {url}') as bar:
        result = check_url_status(url)
        bar.update(1)
    
    if result['reachable']:
        click.secho("✓ URL is reachable", fg='green')
        click.echo(f"Status code: {result['status_code']}")
        click.echo(f"Status: {result['reason']}")
        
        if save_pdf:
            max_retries = 3 if retry else 1
            for attempt in range(max_retries):
                if attempt > 0:
                    click.echo(f"\nRetrying PDF generation (attempt {attempt + 1}/{max_retries})...")
                
                with click.progressbar(length=2, label=f'Saving webpage as PDF') as bar:
                    click.echo("Waiting for page to fully load...")
                    bar.update(1)
                    success, error = save_as_pdf(url, output, timeout)
                    bar.update(1)
                    
                    if success:
                        click.secho(f"✓ PDF saved successfully as '{output}'", fg='green')
                        # Add absolute path information
                        abs_path = os.path.abspath(output)
                        click.secho(f"File location: {abs_path}", fg='blue')
                        break
                    else:
                        if attempt < max_retries - 1:
                            click.secho(f"✗ Attempt failed: {error}", fg='yellow')
                        else:
                            click.secho(f"✗ Failed to save PDF: {error}", fg='red')
    else:
        click.secho("✗ URL is not reachable", fg='red')
        click.secho(f"Reason: {result['reason']}", fg='yellow')

if __name__ == '__main__':
    main()
