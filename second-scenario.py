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
        self.logged_in_message = (By.XPATH, '//div[contains(text(), "Logged in as")]')
        self.delete_account_button = (By.ID, 'deleteAccount')
        self.account_deleted_message = (By.XPATH, '//div[contains(text(), "ACCOUNT DELETED!")]')

    def login(self, email, password):
        self.driver.find_element(*self.email_field).send_keys(email)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text

    def get_logged_in_message(self):
        return self.driver.find_element(*self.logged_in_message).text

    def delete_account(self):
        self.driver.find_element(*self.delete_account_button).click()

    def get_account_deleted_message(self):
        return self.driver.find_element(*self.account_deleted_message).text

def test_login_and_delete_account(browser):
    login_page = LoginPage(browser)
    browser.get("http://automationexercise.com")

    assert "Automation Exercise" in browser.title
    
    signup_login_button = browser.find_element(By.ID, "signupLogin")
    signup_login_button.click()

    assert "Login to your account" in browser.page_source

    login_page.login("test@example.com", "Test1234")

    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(login_page.logged_in_message))

    assert "Logged in as" in login_page.get_logged_in_message()

    login_page.delete_account()

    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(login_page.account_deleted_message))

    assert "ACCOUNT DELETED!" in login_page.get_account_deleted_message()

if __name__ == "__main__":
    pytest.main(["-v", "--html=report.html"])
