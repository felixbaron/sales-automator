"""
Main function for LinkedIn scrapers
"""
import os

import database as Db
from login import login_to_linkedin
from scrapers import get_persons_linkedin, scrape_person, scrape_title
from selenium.webdriver import Chrome
from sqlalchemy import update


def main():
    # Initialize Selenium
    driver = Chrome()
    driver.implicitly_wait(10)

    # Initialize database
    session = Db.initialize()

    # Login to LinkedIn
    login_to_linkedin(driver)

    # Get list of persons
    persons = get_persons_linkedin(driver, os.getenv('ACCOUNT_PAGE'))

    # Scrape persons
    for i in range(len(persons)):
        url = persons[i]['url']
        try:
            person = scrape_person(driver, url)
            Db.add_person(session, person)
        except Exception:
            pass

    # Fetch all records
    query = session.query(Db.Person)
    rows = query.statement.execute().fetchall()

    # Split full_name to first and last
    Db.update_first_and_last(session)

    # Iterate over records and update title
    for row in rows:
        title = scrape_title(driver, row.linkedin_url)
        stmt = (
            update(Db.Person).
            where(Db.Person.id == row.id).
            values(job_title=title)
        )
        stmt.execute()


if __name__ == '__main__':
    main()
