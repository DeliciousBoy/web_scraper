from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

def setup_driver():
    """
    Setup Chrome driver and set to work in bakcground
    """

    options = Options()
    options.add_argument("--headless=new") # Use 'new' flag for the latest headless mode
    options.add_argument("--disable-gpu")  # Disable GPU acceleration (useful in headless mode)
    options.add_argument("--no-sandbox")   # Required for some environments, such as Docker
    options.add_argument("--disable-dev-shm-usage") # Overcome limited resource problems
    
    try:
        driver = webdriver.Chrome(options=options)
        wait = WebDriverWait(driver, 10)
        return driver, wait
    
    except Exception as e:
        print(f'Error setting up the driver: {e}')
        return None, None