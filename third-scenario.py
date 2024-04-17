import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_field = (By.ID, 'email')
        self.password_field = (By.ID, 'password')
        self.login_button = (By.ID, 'login')
        self.error_message = (By.ID, 'loginError')

    def login_with_invalid_credentials(self, email, password):
        self.driver.find_element(*self.email_field).send_keys(email)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.signup_login_button = (By.ID, 'signupLogin')

    def click_signup_login(self):
        self.driver.find_element(*self.signup_login_button).click()

def test_login_with_invalid_credentials(browser):
    browser.get("http://automationexercise.com")

    home_page = HomePage(browser)
    home_page.click_signup_login()

    login_page = LoginPage(browser)

    assert "Login to your account" in browser.page_source

    login_page.login_with_invalid_credentials("invalid@example.com", "InvalidPassword123")

    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(login_page.error_message))
    assert "Your email or password is incorrect!" in login_page.get_error_message()

if __name__ == "__main__":
    pytest.main(["-v", "--html=report.html"])
