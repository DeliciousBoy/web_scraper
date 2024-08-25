import time
from pathlib import Path

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# from locators.product_page import ProductPage
from pages.product_page import ProductPage
from module.element import *


def setup_driver():
    """
    Setup Chrome driver and set to work in bakcground
    """
    options = Options()
    # options.add_argument("--headless=new") # Use 'new' flag for the latest headless mode
    # options.add_argument("--disable-gpu")  # Disable GPU acceleration (useful in headless mode)
    # options.add_argument("--no-sandbox")   # Required for some environments, such as Docker
    # options.add_argument("--disable-dev-shm-usage") # Overcome limited resource problems

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)
    return driver, wait

def scroll_down(driver) -> None:
    """
    Scrolls down the webpage repeatedly until no more new content is loaded.
    """
    
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    while True:
        # Scroll down to the bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        # Wait to load the page
        time.sleep(2)  # Using sleep to give time for content to load

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break  # If no more content is loaded, exit the loop
        last_height = new_height
    
def get_product_links(driver) -> list[str]:
    grid_element = driver.find_element(By.CLASS_NAME, ALL_PRODUCT)
    product_elements = grid_element.find_elements(By.CLASS_NAME, PRODUCT_LIST)
    links = [product_element.find_element(By.XPATH, PRODUCT_LINK).get_attribute('href')
             for product_element in product_elements]
    return links

def extract_product_info(driver):
    p_name = driver.find_element(By.XPATH, PRODUCT_NAME).text
    p_id = driver.find_element(By.XPATH, PRODUCT_ID).text
    p_size = driver.find_element(By.XPATH, PRODUCT_SIZE).text
    p_weight = driver.find_element(By.XPATH, PRODUCT_WEIGHT).text
    p_price = driver.find_element(By.XPATH, PRODUCT_PRICE).text
    p_unit = driver.find_element(By.CLASS_NAME, PRODUCT_PRICE_UNIT).text
    p_promo = [p.text for p in driver.find_elements(By.CSS_SELECTOR, PRODUCT_PROMOTIONS)]
    p_model = next((word for word in PRODUCT_MODEL if word in p_name), 'อื่นๆ')
    return p_name, p_id, p_size, p_weight, p_price, p_unit, p_promo, p_model

def scrape_products():
    driver, wait = setup_driver()
    driver.get(WEB)
    scroll_down(driver)

    links = get_product_links(driver)
    
    df = pd.DataFrame(columns=['name', 'id', 'size', 'weight', 
                               'model', 'price', 'unit', 'promotion', 
                               'detail'])

    for link in links:
        driver.get(str(link))
        p_name, p_id, p_size, p_weight, p_price, p_unit, p_promo, p_model = extract_product_info(driver)
        
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, SEE_MORE_BUTTON))).click()
        p_detail = [d.text for d in driver.find_elements(By.CSS_SELECTOR, PRODUCT_DETAILS)]
        
        df.loc[len(df)] = [p_name, p_id, p_size, p_weight, p_model, p_price, p_unit, p_promo, p_detail]

    driver.quit()
    df.to_excel('products_test_detail.xlsx', index=False)

def main() -> None:
    driver, wait = setup_driver()
    driver.get(WEB)
    scroll_down(driver)
    links = get_product_links(driver)
    for link in links:
        print(driver.get(str(link)))
    
    
if __name__ == "__main__":
    main()