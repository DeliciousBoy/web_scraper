from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from src.config_loader import ScraperSelector

def get_all_product_links(driver, selector: ScraperSelector):
    """
    Extract all product links from the main page.
    """

    try:   
        grid_element = driver.find_element(By.CLASS_NAME, selector.all_product_class)
        product_elements = grid_element.find_elements(By.CLASS_NAME, selector.product_list_class)
        links = [product_element.find_element(By.XPATH, selector.product_link_path).get_attribute('href')
                for product_element in product_elements]
        return links

    except NoSuchElementException as e:
        print(f'An error occurred while trying to find elements: {e}')
        return []