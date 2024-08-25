import yaml
from pathlib import Path
from dataclasses import dataclass
from typing import Union

@dataclass()
class ScraperSelector:
    all_product_class: str
    product_list_class: str
    product_link_path: str

def load_config(*, config_path: Union[str, Path]) -> ScraperSelector:
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
        
        return selector

    except FileNotFoundError:
        print(f'Error: the file {config_path} was not found')
        raise

    except yaml.YAMLError as e:
        print(f'Error parsing YAML file: {e}')
        raise



