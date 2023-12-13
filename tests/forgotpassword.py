from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time
from pageobject.forgotpasswordpage import LoginPage

class TestForgotPassword(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install())
        )
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        self.base_url = "https://dev-hse.apps-madhani.com/login"
    
    # Forgot Password page Validation
    def test_fpass_1(self):
        driver = self.driver
        driver.get(self.base_url)
        forgetpage = TestForgotPassword(driver)