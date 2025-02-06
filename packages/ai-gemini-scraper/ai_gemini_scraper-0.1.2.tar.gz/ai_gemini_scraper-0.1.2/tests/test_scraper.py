import unittest
from ai_scraper import scrape

class TestScraper(unittest.TestCase):
    def test_scrape_function_exists(self):
        self.assertTrue(callable(scrape))

if __name__ == '__main__':
    unittest.main()
