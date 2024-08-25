import yaml
from pathlib import Path
from dataclasses import dataclass
from typing import Union, Tuple, Optional

@dataclass()
class ScraperSelector:
    """ Dataclass for storing Classname and XPATH selectors for scraping."""
    all_product_class: str
    product_list_class: str
    product_link_path: str

@dataclass
class ProductElements:
    """ Dataclass for storing product element selectors."""
    name: str
    id: str
    size: str
    weight: str
    price: str
    unit: str

def load_config(*, config_path: Union[str, Path]) -> Tuple[ScraperSelector, ProductElements, Optional[str]]:
    """
    Load the YAML configuration file and return a config object.
    """

    try:
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)

        selector = ScraperSelector(
            all_product_class=config['selector']['all_product_class'],
            product_list_class=config['selector']['product_list_class'],
            product_link_path=config['selector']['product_link_path'],
        )

        element = ProductElements(
            name=config['product_element']['name'],
            id=config['product_element']['id'],
            size=config['product_element']['size'],
            weight=config['product_element']['weight'],
            price=config['product_element']['price'],
            unit=config['product_element']['unit'],    
        )

        web_url = config['web_url']
        return selector, element, web_url

    except FileNotFoundError:
        print(f'Error: the file {config_path} was not found')
        raise

    except yaml.YAMLError as e:
        print(f'Error parsing YAML file: {e}')
        raise



