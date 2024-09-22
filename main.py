from selenium import webdriver
from selenium.webdriver.common.by import By
from base.locators import Locators as l
from base.base_page import BasePage
import json
import time


driver = webdriver.Firefox()
with open('data.json', 'r') as file:
    data = json.load(file)

first_name = data["First name"]
last_name = data["Last name"]
phone = data["Phone"]
resume_file = data["Resume"]
email = data["Email"]

# Open the URL
link = input("Please enter the link: ")
driver.get(link)
driver.implicitly_wait(5)  

# Actions
base_page = BasePage(driver)
base_page.enter_text(*l.FIRST_NAME, first_name)
base_page.enter_text(*l.LAST_NAME, last_name)
base_page.enter_text(*l.EMAIL, email)
base_page.enter_text(*l.PHONE, phone)
base_page.click_element(*l.ATTACH_BUTTON)
resume_input = driver.find_element(*l.RESUME_TEXT)
resume_input.send_keys(resume_file)

# base_page.click_element(*l.SUBMIT_BUTTON)
