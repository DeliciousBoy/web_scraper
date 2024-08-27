from src.setup_driver import setup_driver
from src.config_loader import load_config
from src.scroll_down import scroll_down
from src.get_all_product_links import get_all_product_links
from src.config_loader import load_config
from src.product_scraper import scrape_product_data
from src.save_to_csv import save_product_data_to_csv

def main() -> None:  
   driver, wait = setup_driver()
   try:
      selector, category_config = load_config(config_path='config.yaml', category='roofing_equipment')
      driver.get(category_config.web_url)
      scroll_down(driver)
      product_links = get_all_product_links(driver=driver, selector=selector)
      product_data_list = scrape_product_data(driver=driver, product_links=product_links, elements=category_config.product_elements)
      save_product_data_to_csv(product_data_list, output_path='product_report_1.csv')
   finally:
      driver.quit()

if __name__ == "__main__":
    main()