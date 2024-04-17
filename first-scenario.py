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

class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_field = (By.ID, 'firstname')
        self.last_name_field = (By.ID, 'lastname')
        self.email_field = (By.ID, 'email_address')
        self.password_field = (By.ID, 'password')
        self.confirm_password_field = (By.ID, 'password-confirmation')
        self.register_button = (By.CSS_SELECTOR, 'button[title="Register"]')
        self.success_message = (By.CSS_SELECTOR, '.message-success')

    def fill_registration_form(self, first_name, last_name, email, password):
        self.driver.find_element(*self.first_name_field).send_keys(first_name)
        self.driver.find_element(*self.last_name_field).send_keys(last_name)
        self.driver.find_element(*self.email_field).send_keys(email)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.confirm_password_field).send_keys(password)

    def click_register_button(self):
        self.driver.find_element(*self.register_button).click()

    def get_success_message(self):
        return self.driver.find_element(*self.success_message).text

def test_registration(browser):
    registration_page = RegistrationPage(browser)
    registration_page.fill_registration_form("John", "Doe", "john.doe@example.com", "Test1234")
    registration_page.click_register_button()
    
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(registration_page.success_message))
    
    assert "Thank you for registering" in registration_page.get_success_message()

if __name__ == "__main__":
    pytest.main(["-v", "--html=report.html"])
