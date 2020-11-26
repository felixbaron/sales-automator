"""
This Python script automates Salesforce contact creation.
"""


import os

from selenium.webdriver.common.keys import Keys


def create_contact(
        driver, account_id, first, last, phone, title, about, city, url):
    """Creates a contact record in Salesforce, individual to layout"""
    # Create new contact
    account_url = os.getenv('SALESFORCE_URL') + '/' + account_id
    driver.get(account_url)
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    driver.find_element_by_name('new_contact').click()

    # Fill fields for new contact and save
    driver.find_element_by_class_name('email').send_keys(
        '', Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, first)
    driver.find_element_by_class_name('lastName').send_keys(
        last, Keys.TAB, city, Keys.TAB, title, Keys.TAB, Keys.TAB,
        phone)
    driver.find_element_by_css_selector('input.btn[value="Save"]').click()

    # Edit contact
    driver.find_element_by_name('edit').click()
    driver.find_element_by_css_selector('input#name_firstcon2').send_keys(
        Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, about)
    driver.find_element_by_css_selector('input#con4').send_keys(
        Keys.TAB, Keys.TAB, Keys.TAB, url)
    driver.find_element_by_css_selector('input[title="Save"]').click()


def log_a_call(driver, contact_id, subject, notes, call_type):
    """Logs a call at a contact, individual to Layout"""
    if (contact_id):
        driver.get(os.getenv('SALESFORCE_URL') + contact_id)
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    driver.find_element_by_css_selector(
        'input.btn[value="Log a Call"]').click()
    driver.find_element_by_css_selector('#tsk5').send_keys(subject)
    driver.find_element_by_css_selector('#tsk6').send_keys(notes)
    # For type LinkedIn Mail=L
    driver.find_element_by_css_selector('#tsk10').send_keys(call_type)
    driver.find_element_by_css_selector('input.btn[title="Save"]').click()
