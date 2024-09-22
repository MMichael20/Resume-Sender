from selenium.webdriver.remote.webdriver import WebDriver

class BasePage():
      def __init__(self, driver:WebDriver) -> None:
            self.driver = driver
            
      def click_element(self, locator_type, locator_value):
            self.driver.find_element(locator_type, locator_value).click()
            
      def enter_text(self, locator_type, locator_value, text):
            self.driver.find_element(locator_type, locator_value).clear()
            self.driver.find_element(locator_type, locator_value).send_keys(text)
            