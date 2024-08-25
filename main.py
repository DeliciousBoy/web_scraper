import time
from pathlib import Path

import pandas as pd
import yaml
from selenium import webdriver

from src.element import *

from src.config_loader import load_config
from src.setup_driver import setup_driver
from src.scroll_down import scroll_down
from src.get_all_product_links import get_all_product_links


def main() -> None:

    driver, wait = setup_driver()
    selector = load_config(config_path='config.yaml')
    try:
        driver.get(WEB)
        scroll_down(driver, wait)
        links = get_all_product_links(driver, selector)
        for i, link in enumerate(links):
            print(i, link)
    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        driver.quit()    

    
if __name__ == "__main__":
    main()