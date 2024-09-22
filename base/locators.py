from selenium.webdriver.common.by import By

class Locators:
    FIRST_NAME = (By.CSS_SELECTOR, 'input[id="first_name"]')
    LAST_NAME = (By.CSS_SELECTOR, 'input[id="last_name"]')
    EMAIL = (By.CSS_SELECTOR, 'input[id="email"]')
    PHONE = (By.CSS_SELECTOR, 'input[id="phone"]')
    RESUME_TEXT = (By.CSS_SELECTOR, 'textarea[name="resume_text"]')
    ATTACH_BUTTON = (By.XPATH, '//button[@data-source="attach"]')
    SUBMIT_BUTTON = (By.XPATH, '//button[contains(text(), "Submit")]')
