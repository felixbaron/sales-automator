"""
Automates LinkedIn with Selenium
"""


def connect_on_linkedin(driver, url):
    """Connect with LinkedIn profile"""
    driver.get(url)
    try:
        driver.find_element_by_css_selector(
            'button[aria-label*="Connect"]').click()
        driver.find_element_by_css_selector(
            'button[aria-label*="Send"]').click()
    except Exception:
        try:
            driver.find_element_by_css_selector(
                '.pv-s-profile-actions__overflow-toggle').click()
            driver.find_element_by_css_selector(
                'li-icon[type="connect-icon"]').click()
            driver.find_element_by_css_selector(
                'button[aria-label*="Send"]').click()
        except Exception:
            pass
