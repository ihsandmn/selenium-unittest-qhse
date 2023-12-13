from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    def valid_login_page(self):
        self.driver.find_element(By.CSS_SELECTOR, ".styles_header__v6y_t.styles_header__vXte2")
        self.driver.find_element(By.CSS_SELECTOR, ".ant-typography.styles_root__AoSOf.css-4j6e0i[shub-ins='1']")
        self.driver.find_element(By.CSS_SELECTOR, "#nik")
        self.driver.find_element(By.CSS_SELECTOR, "#password")
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        self.driver.find_element(By.CSS_SELECTOR, ".styles_image__PtV_D")
    
    def input_login_with(self,nik,password):
        self.driver.find_element(By.CSS_SELECTOR, "#nik").send_keys(nik)
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    
    def click_submit(self):
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        
    def error_message_nik(self):
        element = self.driver.find_element(By.CSS_SELECTOR, ".ant-form-item-explain-error")
        assert element.text == "User not found."
    
    def error_message_password(self):
        element = self.driver.find_element(By.CSS_SELECTOR, ".ant-form-item-explain-error")
        assert element.text == "Wrong password."

    def error_message_blank(self):
        element = self.driver.find_element(By.CSS_SELECTOR, ".ant-form-item-explain-error[shub-ins='1']")
        assert element
    
    def open_forgot_password(self):
        self.driver.find_element(By.CSS_SELECTOR, ".ant-typography.css-4j6e0i[shub-ins='1']").click()
    
    def validate_forgot_password(self):
        self.driver.find_element(By.CSS_SELECTOR, ".ant-typography.styles_root__AoSOf.css-4j6e0i[shub-ins='1']")