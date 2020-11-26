"""
This Selenium script helps to extract the list of contacts from an account
based search from Sales Navigator.
"""


import os

from selenium.webdriver.common.by import By


def to_linkedin(driver):
    """Logs in to LinkedIn"""
    driver.get('https://linkedin.com/sales/login')
    iframe = driver.find_element(By.CSS_SELECTOR, "body > iframe")
    driver.switch_to.frame(iframe)
    elem_username = driver.find_element_by_id('username')
    elem_username.send_keys(os.getenv('LINKEDIN_USER'))
    elem_password = driver.find_element_by_id('password')
    elem_password.send_keys(os.getenv('LINKEDIN_PWD'))
    driver.find_element_by_class_name('login__form_action_container').click()
