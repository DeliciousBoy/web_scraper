import pandas as pd

from src.setup_driver import setup_driver
from src.scroll_down import scroll_down
from src.get_all_product_links import get_all_product_links
from src.config_loader import load_config

def ex():

    # Load configuration
    selector, element, web_url = load_config(config_path='config.yaml')
    driver, wait = setup_driver()
    driver.get(web_url)
    scroll_down(driver)

    links = get_all_product_links(driver, selector)
    
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