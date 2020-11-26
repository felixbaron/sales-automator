"""
Main function for LinkedIn scrapers
"""
import os

import database as Db
import linkedin
import login
import salesforce as sf
from environ import set_env
from scrapers import get_persons_linkedin, get_profile_linkedin, get_title
from selenium.webdriver import Chrome
from sqlalchemy import update

set_env()


def main():
    # Initialize Selenium
    driver = Chrome()
    driver.implicitly_wait(15)

    # Initialize database
    session = Db.initialize()

    # Login to LinkedIn
    login.to_linkedin(driver)
    login.to_Salesforce(driver)

    # Get list of persons
    persons = get_persons_linkedin(driver, os.getenv('ACCOUNT_PAGE'))

    # Scrape persons
    for i in range(len(persons)):
        url = persons[i]['url']
        try:
            person = get_profile_linkedin(driver, url)
            Db.add_person(session, person)
        except Exception:
            pass

    Db.update_first_and_last(session)

    # Fetch all rows from database
    rows = Db.fetch_all(session, Db.Person)

    # Iterate over records and update title
    for row in rows:
        title = get_title(driver, row.linkedin_url)
        stmt = (
            update(Db.Person).
            where(Db.Person.id == row.id).
            values(job_title=title)
        )
        stmt.execute()

    # Read duplicates, LinkedIn URLs as csv
    dupes = Db.read_csv_file_as_list('./dupes.csv')

    # Create contacts in Salesoforce
    for c in rows:
        if [c['linkedin_url']] not in dupes:
            sf.create_contact(driver, account_id=os.getenv('ACCOUNT_ID'),
                              first=c['first'], last=c['last'],
                              title=c['job_title'],  url=c['linkedin_url'],
                              city=c['location'], about=c['about'],
                              phone='123')
            sf.log_a_call(driver, None, 'LinkedIn connect',
                          'Requested to connect', 'L')
    # Connect on LinkedIn
    for c in rows:
        # Connect on LinkedIn
        linkedin.connect_on_linkedin(driver, c['linkedin_url'])


if __name__ == '__main__':
    main()
