import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_login_and_delete_account(browser):
    # Step 1: Launch browser
    browser.get("http://automationexercise.com")

    # Step 2: Navigate to url 'http://automationexercise.com'
    assert "Automation Exercise" in browser.title  # Step 3: Verify that home page is visible successfully

    # Step 4: Click on 'Signup / Login' button
    signup_login_button = browser.find_element(By.ID, "signupLogin")
    signup_login_button.click()

    # Step 5: Verify 'Login to your account' is visible
    assert "Login to your account" in browser.page_source

    # Step 6: Enter correct email address and password
    email_input = browser.find_element(By.ID, "email")
    password_input = browser.find_element(By.ID, "password")
    email_input.send_keys("test@example.com")
    password_input.send_keys("Test1234")

    # Step 7: Click 'login' button
    login_button = browser.find_element(By.ID, "login")
    login_button.click()

    # Step 8: Verify that 'Logged in as username' is visible
    assert "Logged in as" in browser.page_source

    # Step 9: Click 'Delete Account' button
    delete_account_button = browser.find_element(By.ID, "deleteAccount")
    delete_account_button.click()

    # Step 10: Verify that 'ACCOUNT DELETED!' is visible
    time.sleep(2)  # Wait for the account deletion process to complete
    assert "ACCOUNT DELETED!" in browser.page_source

if __name__ == "__main__":
    pytest.main(["-v", "--html=report.html"])
