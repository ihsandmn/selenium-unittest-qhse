from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time
from pageobject.forgotpasswordpage import FpasswordPage

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
        forgetpage = FpasswordPage(driver)
        forgetpage.forgot_password_page_valid
        time.sleep(1)

    # # Input valid email to recover the password
    # def test_fpass_2(self):