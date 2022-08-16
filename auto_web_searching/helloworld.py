import pathlib
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

DRIVER_PATH = pathlib.Path().parent.absolute() / 'chromedriver' / 'chromedriver.exe'

class HelloWorld(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver =  webdriver.Chrome(executable_path=DRIVER_PATH)
        driver = cls.driver
        driver.implicitly_wait(10)

    def test_hello_world(self):
        driver = self.driver
        driver.get('https://en.wikipedia.org/wiki/%22Hello,_World!%22_program')
    
    def test_visit_google(self):
        driver = self.driver
        driver.get('https://www.google.com')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reports', report_name='hello-world-report'))