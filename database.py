"""
This is a database helper on AlechemySQL and PostgreSQL.
"""

import os

from sqlalchemy import Column, Integer, String, create_engine, update
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Data manipulators


def split_name(fullname):
    """Splits full name in first and last"""
    last = fullname.strip().split(' ')[-1]
    first = fullname.strip().split(' ')
    del first[-1]
    first = ' '.join(first)
    return {first, last}


def update_first_and_last(session):
    """Updates first and last name"""
    query = session.query(Person)
    rows = query.statement.execute().fetchall()
    for row in rows:
        first, last = split_name(row.full_name)
        stmt = (
            update(Person).
            where(Person.id == row.id).
            values(first=first, last=last)
        )
        stmt.execute()


# Database helpers


class Person(Base):
    """Person representation for PostgreSQL"""
    __tablename__ = 'persons'
    # Columns
    id = Column(Integer, primary_key=True)
    first = Column(String)
    last = Column(String)
    company = Column(String)
    about = Column(String)
    accomplishments = Column(String)
    also_viewed_urls = Column(String)
    contacts = Column(String)
    educations = Column(String)
    experiences = Column(String)
    interests = Column(String)
    job_title = Column(String)
    linkedin_url = Column(String)
    location = Column(String)
    full_name = Column(String)


def initialize():
    """Inititalizes the database"""
    engine = create_engine(
        'postgresql+psycopg2://postgres:' + os.getenv('POSTGRES_PWD') + '\
@localhost:5432/postgres', echo=False)
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine
    DBSession = sessionmaker()
    DBSession.bind = engine
    session = DBSession()
    return session


def add_person(session, person):
    """Adds a person record"""
    person = Person(
        about=str(person.about),
        accomplishments=str(person.accomplishments),
        also_viewed_urls=str(person.also_viewed_urls),
        company=person.company,
        # TODO: transform to array of names
        # contacts=str(person.contacts),
        educations=str(person.educations),
        experiences=str(person.experiences),
        interests=str(person.interests),
        job_title=str(person.job_title),
        linkedin_url=str(person.linkedin_url),
        location=str(person.location),
        full_name=str(person.name)
    )
    session.add(person)
    session.commit()
