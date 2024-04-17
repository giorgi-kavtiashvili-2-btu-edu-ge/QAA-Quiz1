import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_login_with_incorrect_credentials(browser):
    # Step 1: Launch browser
    browser.get("http://automationexercise.com")

    # Step 2: Navigate to url 'http://automationexercise.com'
    assert "Automation Exercise" in browser.title  # Step 3: Verify that home page is visible successfully

    # Step 4: Click on 'Signup / Login' button
    signup_login_button = browser.find_element(By.ID, "signupLogin")
    signup_login_button.click()

    # Step 5: Verify 'Login to your account' is visible
    assert "Login to your account" in browser.page_source

    # Step 6: Enter incorrect email address and password
    email_input = browser.find_element(By.ID, "email")
    password_input = browser.find_element(By.ID, "password")
    email_input.send_keys("incorrect@example.com")
    password_input.send_keys("IncorrectPassword123")

    # Step 7: Click 'login' button
    login_button = browser.find_element(By.ID, "login")
    login_button.click()

    # Step 8: Verify error 'Your email or password is incorrect!' is visible
    error_message = browser.find_element(By.ID, "loginError").text
    assert "Your email or password is incorrect!" in error_message

if __name__ == "__main__":
    pytest.main(["-v", "--html=report.html"])
