from selenium.webdriver.common.by import By

from element import *

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