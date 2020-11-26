# Sales Automator

## About

This scraper helps to:

- login to LinkedIn / Sales Navigator
- extract contacts from Sales Navigator
- extract LinkedIn profiles
- load data in PostgreSQL database

## Installation

Install [PostgreSQL](https://www.postgresql.org/download/) and Python requirements.

```shell
python3 -m pip install sqlalchemy linkedin_scraper selenium clipboard psycopg2
```

## Usage

Set environment variables:

```py
import os

# LinkedIn credentials
os.environ['USER'] = 'myuser'
os.environ['LINKEDIN_USER'] = 'myuser'
os.environ['LINKEDIN_PWD'] = 'mysec'
os.environ['POSTGRES_PWD'] = 'mysec'

# Account page for Salesforce
os.environ['ACCOUNT_ID'] = '123'

# Salesforce tenant
os.environ['SALESFORCE_URL'] = '123'

# Account page for LinkedIn
os.environ['ACCOUNT_PAGE'] = '123'
```

Start script

Through Python:

```py
from main import main
main()
```

Or with Shell:

```shell
python3 main.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to test as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
