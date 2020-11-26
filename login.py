"""
This Selenium script helps to extract the list of contacts from an account
based search from Sales Navigator.
"""


import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def to_linkedin(driver):
    """Logs in securely to LinkedIn"""
    driver.get('https://www.linkedin.com/login')
    user = os.getenv('LINKEDIN_USER')
    pwd = os.getenv('LINKEDIN_PWD')
    driver.find_element_by_css_selector('#username').send_keys(user)
    driver.find_element_by_css_selector(
        '#password').send_keys(pwd)
    driver.find_element_by_css_selector(
        '#password').send_keys(Keys.ENTER)


def to_navigator(driver):
    """Logs in to LinkedIn"""
    driver.get('https://linkedin.com/sales/login')
    iframe = driver.find_element(By.CSS_SELECTOR, "body > iframe")
    driver.switch_to.frame(iframe)
    elem_username = driver.find_element_by_id('username')
    elem_username.send_keys(os.getenv('LINKEDIN_USER'))
    elem_password = driver.find_element_by_id('password')
    elem_password.send_keys(os.getenv('LINKEDIN_PWD'))
    driver.find_element_by_class_name('login__form_action_container').click()


def to_Salesforce(driver):
    """Logs in securly to Salesforce with manual entries"""
    driver.get(os.getenv('SALESFORCE_URL'))
    time.sleep(15)
