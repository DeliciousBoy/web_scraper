import unittest
from pathlib import Path

from loguru import logger

from src.config_loader import load_config, ScraperSelector, CategoryConfig

class TestLoadConfig(unittest.TestCase):

    def setUp(self):
        # กำหนด path ของไฟล์ config ที่จะใช้ใน unittest
        self.config_path = Path('config.yaml')

    def test_load_valid_category(self):
        category = 'ceramic'  # หมวดหมู่ที่เรารู้ว่าอยู่ใน config.yaml
        selector, category_config = load_config(self.config_path, category)
        
        self.assertIsInstance(selector, ScraperSelector)
        self.assertIsInstance(category_config, CategoryConfig)
        self.assertEqual(category_config.web_url, 'https://www.scghome.com/products/subcategory/...')
        # ตรวจสอบค่าอื่นๆ ใน category_config.product_elements ตามที่คาดหวัง
        self.assertEqual(category_config.product_elements.name, 'ProductDescription_displayName__ztjNk')

    def test_load_invalid_category(self):
        category = 'invalid_category'  # หมวดหมู่ที่ไม่ควรอยู่ใน config.yaml
        with self.assertRaises(ValueError) as context:
            load_config(self.config_path, category)
        self.assertTrue(f'Category "{category}" not found in config.' in str(context.exception))

    def test_missing_config_file(self):
        invalid_path = Path('missing_config.yaml')
        with self.assertRaises(FileNotFoundError) as context:
            load_config(invalid_path, 'ceramic')
        self.assertTrue(f'Error: the file {invalid_path} was not found' in str(context.exception))

    def test_invalid_yaml_format(self):
        # สมมุติว่าเรามีไฟล์ YAML ที่รูปแบบไม่ถูกต้อง
        invalid_yaml_path = Path('invalid_config.yaml')
        with open(invalid_yaml_path, 'w') as file:
            file.write("invalid_yaml: [missing_end_bracket")
        
        with self.assertRaises(Exception) as context:
            load_config(invalid_yaml_path, 'ceramic')
        self.assertTrue('Error parsing YAML file' in str(context.exception))
        
        # ลบไฟล์ที่สร้างขึ้น
        invalid_yaml_path.unlink()

if __name__ == '__main__':
    unittest.main()
