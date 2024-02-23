from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import HTMLTestRunner
import unittest
import time
from pageobject.loginpage import LoginPage

# MTNC-61 Execute test Login page
class TestLogin(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install())
        )
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.base_url = "https://dev-hse.apps-madhani.com/login"

    # Login page Validation
    def test_login_1(self):
        driver = self.driver
        driver.get(self.base_url)
        loginpage = LoginPage(driver)
        self.assertEqual("Login - QHSE", self.driver.title, "Web title not matching")
        self.assertTrue(loginpage.valid_login_page)
        time.sleep(1)

    # Login with valid account
    def test_login_2(self):
        driver = self.driver
        driver.get(self.base_url)
        loginpage = LoginPage(driver)
        loginpage.input_login_with("fcb006","test123")
        time.sleep(4)
        self.assertEqual("Under Construction - QHSE", self.driver.title, "Web title not matching")
    
    # Login with invalid NIK
    def test_login_3(self):
        driver = self.driver
        driver.get(self.base_url)
        loginpage = LoginPage(driver)
        loginpage.input_login_with("fcb0078","test123")
        loginpage.error_message_nik
        time.sleep(1)
    
    # Login with invalid NIK
    def test_login_4(self):
        driver = self.driver
        driver.get(self.base_url)
        loginpage = LoginPage(driver)
        loginpage.input_login_with("Fx#0000000001","test123")
        loginpage.error_message_nik
        time.sleep(1)

    # Login with invalid Password
    def test_login_5(self):
        driver = self.driver
        driver.get(self.base_url)
        loginpage = LoginPage(driver)
        loginpage.input_login_with("12345","test12sd3")
        loginpage.error_message_password
        time.sleep(1)
    
    # Login without input any value on the fields
    def test_login_6(self):
        driver = self.driver
        driver.get(self.base_url)
        loginpage = LoginPage(driver)
        loginpage.click_submit
        loginpage.error_message_blank
        time.sleep(1)
    
    # Show and Hide password value
    def test_login_7(self):
        driver = self.driver
        driver.get(self.base_url)
        loginpage = LoginPage(driver)
        loginpage.open_forgot_password
        self.assertTrue(loginpage.validate_forgot_password)
    
    def test_login_8(self):
        driver = self.driver
        driver.get(self.base_url)
        loginpage = LoginPage(driver)
        

    @classmethod
    def tearDown(self):
        self.driver.quit


if __name__ == "__main__":
    unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output="../reports"))

