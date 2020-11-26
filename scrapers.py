import time

import clipboard
from linkedin_scraper import Person

# Helper functions


def is_iteratable(button):
    """Checks if the list continues"""
    classes = button.get_attribute('class')
    if (classes.find('disabled') == -1):
        return True
    else:
        return False


def scrape_title(driver, url):
    """Rescrapes the title only"""
    driver.get(url)
    time.sleep(2)
    element = driver.find_element_by_css_selector('h2:nth-child(2)')
    return element.text


def navigator_to_linkedin(driver, url):
    """Copies LinkedIn URL of a contact"""
    driver.get(url)
    linkedin_actions = driver.find_element_by_css_selector(
        'li-icon[aria-label="More actions"] svg')
    linkedin_actions.click()
    linkedin_url = driver.find_element_by_xpath(
        "//*[text()='Copy LinkedIn.com URL']")
    linkedin_url.click()
    time.sleep(1)
    return clipboard.paste()


# Scrapers


def get_persons_navigator(driver, url):
    """Scrapes all contacts from an acount search"""
    driver.get(url)
    persons = []
    # Scroll to end of page
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    for i in range(4):
        driver.execute_script('window.scrollBy(0, -900);')
        time.sleep(1)
    table = driver.find_elements_by_css_selector('.result-lockup \
.result-lockup__name a')
    for person in table:
        url = person.get_attribute('href')
        persons.append({'url': url})
    return persons


def get_persons_linkedin(driver, url):
    """Scrapes all contacts from a certain account page"""
    # Visit account page
    driver.get(url)
    # Scroll to bottom of page
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    # Find Next button
    button = driver.find_element_by_css_selector('button[aria-label="Next"]')
    # Extract all persons unless Next button is disabled
    persons = []
    while (is_iteratable(button)):
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        table = driver.find_elements_by_css_selector(
            '.search-result__image-wrapper a')
        for person in table:
            url = person.get_attribute('href')
            persons.append({'url': url})
        button.click()
        time.sleep(3)
        button = driver.find_element_by_css_selector(
            'button[aria-label="Next"]')
    return persons


def get_profile_linkedin(driver, url):
    """Scrapes a person"""
    person = Person(
        linkedin_url=url, name=None, about=[], experiences=[],
        educations=[], interests=[], accomplishments=[], company=None,
        job_title=None, driver=driver, scrape=False)
    person.scrape(close_on_complete=False)
    return person
