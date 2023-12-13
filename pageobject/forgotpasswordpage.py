from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class FpasswordPage:
    def __init__(self,driver):
        self.driver = driver
    
    def forgot_password_page_valid(self):
        self.driver.find_element(By.CSS_SELECTOR, ".ant-typography.css-4j6e0i[shub-ins='1']").click()
        self.driver.find_element(By.CSS_SELECTOR, ".styles_header__v6y_t.styles_wrapper__AjMPQ")
        self.driver.find_element(By.CSS_SELECTOR, "h3[class='ant-typography styles_root__AoSOf css-4j6e0i']")
        self.driver.find_element(By.CSS_SELECTOR, "#email")
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        self.driver.find_element(By.CSS_SELECTOR, "a[class='ant-typography css-4j6e0i']")
