from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from typing import Tuple, Optional, Any, Callable
from functools import wraps
import time
import logging

# Configure webdriver manager logging
logging.getLogger('WDM').setLevel(logging.WARNING)

def get_chrome_driver(window_size: Tuple[int, int] = (1920, 1080)) -> webdriver.Chrome:
    """Create and configure Chrome driver with common options."""
    options = webdriver.ChromeOptions()
    # Set binary location to Chrome instead of Chromium
    options.binary_location = "/usr/bin/google-chrome"
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument(f'--window-size={window_size[0]},{window_size[1]}')
    options.add_argument('--hide-scrollbars')
    
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)

def with_driver(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator to handle driver creation and cleanup."""
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        driver = None
        try:
            driver = get_chrome_driver()
            if 'driver' in kwargs:
                kwargs['driver'] = driver
            else:
                kwargs = {**kwargs, 'driver': driver}
            return func(*args, **kwargs)
        except Exception as e:
            return False, str(e)
        finally:
            if driver:
                driver.quit()
    return wrapper

def wait_for_page_load(driver: webdriver.Chrome, timeout: int = 30) -> bool:
    """Wait for page to be fully loaded."""
    try:
        # Wait for initial page load
        WebDriverWait(driver, timeout).until(
            lambda d: d.execute_script('return document.readyState') == 'complete'
        )
        
        # Check for dynamic content
        WebDriverWait(driver, timeout).until(lambda d: d.execute_script("""
            return (
                document.readyState === 'complete' &&
                !document.querySelector('.loading') &&
                !document.querySelector('[data-loading]') &&
                (window.jQuery ? !jQuery.active : true) &&
                (!window.angular || !angular.element(document).injector() || 
                 !angular.element(document).injector().get('$http').pendingRequests.length)
            )
        """))
        return True
    except TimeoutException:
        return False

def scroll_page(driver: webdriver.Chrome, retries: int = 3, wait_time: int = 2) -> int:
    """Scroll page to load all lazy content and return final height."""
    last_height = 0
    retry_count = retries
    
    while retry_count > 0:
        new_height = driver.execute_script("""
            window.scrollTo(0, document.documentElement.scrollHeight);
            return document.documentElement.scrollHeight;
        """)
        
        if new_height == last_height:
            retry_count -= 1
        else:
            last_height = new_height
            retry_count = retries
            
        time.sleep(wait_time)
    
    return last_height
