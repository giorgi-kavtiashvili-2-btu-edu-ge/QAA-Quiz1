import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_signup_and_delete_account(browser):
    # Step 1: Launch browser
    browser.get("http://automationexercise.com")
    
    # Step 2: Navigate to url 'http://automationexercise.com'
    assert "Automation Exercise" in browser.title  # Step 3: Verify that home page is visible successfully
    
    # Step 4: Click on 'Signup / Login' button
    signup_login_button = browser.find_element(By.ID, "signupLogin")
    signup_login_button.click()
    
    # Step 5: Verify 'New User Signup!' is visible
    assert "New User Signup!" in browser.page_source
    
    # Step 6: Enter name and email address
    name_input = browser.find_element(By.ID, "name")
    email_input = browser.find_element(By.ID, "email")
    name_input.send_keys("Test User")
    email_input.send_keys("test@example.com")
    
    # Step 7: Click 'Signup' button
    signup_button = browser.find_element(By.ID, "signup")
    signup_button.click()
    
    # Step 8: Verify that 'ENTER ACCOUNT INFORMATION' is visible
    assert "ENTER ACCOUNT INFORMATION" in browser.page_source
    
    # Step 9: Fill details: Title, Name, Email, Password, Date of birth
    title_input = browser.find_element(By.ID, "title")
    password_input = browser.find_element(By.ID, "password")
    dob_input = browser.find_element(By.ID, "dob")
    title_input.send_keys("Mr.")
    password_input.send_keys("Test1234")
    dob_input.send_keys("01/01/1990")
    
    # Step 10: Select checkbox 'Sign up for our newsletter!'
    newsletter_checkbox = browser.find_element(By.ID, "newsletter")
    newsletter_checkbox.click()
    
    # Step 11: Select checkbox 'Receive special offers from our partners!'
    offers_checkbox = browser.find_element(By.ID, "offers")
    offers_checkbox.click()
    
    # Step 12: Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
    first_name_input = browser.find_element(By.ID, "firstName")
    last_name_input = browser.find_element(By.ID, "lastName")
    company_input = browser.find_element(By.ID, "company")
    address_input = browser.find_element(By.ID, "address")
    address2_input = browser.find_element(By.ID, "address2")
    country_input = browser.find_element(By.ID, "country")
    state_input = browser.find_element(By.ID, "state")
    city_input = browser.find_element(By.ID, "city")
    zipcode_input = browser.find_element(By.ID, "zipcode")
    mobile_input = browser.find_element(By.ID, "mobile")
    
    first_name_input.send_keys("John")
    last_name_input.send_keys("Doe")
    company_input.send_keys("Test Company")
    address_input.send_keys("123 Test Street")
    address2_input.send_keys("Apt 101")
    country_input.send_keys("United States")
    state_input.send_keys("California")
    city_input.send_keys("San Francisco")
    zipcode_input.send_keys("12345")
    mobile_input.send_keys("1234567890")
    
    # Step 13: Click 'Create Account' button
    create_account_button = browser.find_element(By.ID, "createAccount")
    create_account_button.click()
    
    # Step 14: Verify that 'ACCOUNT CREATED!' is visible
    assert "ACCOUNT CREATED!" in browser.page_source
    
    # Step 15: Click 'Continue' button
    continue_button = browser.find_element(By.ID, "continue")
    continue_button.click()
    
    # Step 16: Verify that 'Logged in as username' is visible
    assert "Logged in as" in browser.page_source
    
    # Step 17: Click 'Delete Account' button
    delete_account_button = browser.find_element(By.ID, "deleteAccount")
    delete_account_button.click()
    
    # Step 18: Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
    assert "ACCOUNT DELETED!" in browser.page_source
    continue_button = browser.find_element(By.ID, "continue")
    continue_button.click()

if __name__ == "__main__":
    pytest.main(["-v", "--html=report.html"])
