# Twitoff-21

Flask web application to compare a Twitter Users hypothetical tweet.

## Prerequisites

  + Python 3.8
  + Pipenv (`brew install pipenv` to install on mac)
  + SQLite (should be pre-installed on most machines)

## Setup

### Setup Environment

Install package dependencies from existing Pipfile:

```sh
pipenv install
```

Activate the virtual environment:

```sh
pipenv shell
```

### Configuring Environment Variables

Create a new file called ".env".

Obtain [Twitter API Keys](https://developer.twitter.com), then configure environment variables in the ".env" file accordingly:

```sh
# the ".env" file
ENV="development"
FLASK_ENV="development"
DATABASE_URL="sqlite:///db.sqlite3"
TWITTER_API_KEY="______________"
TWITTER_API_KEY_SECRET="__________"
```

### Setup the Database

Using the [`Flask-Migrate` package](https://flask-migrate.readthedocs.io/en/latest/) to simplify database creation and migration:

```sh
#pipenv install Flask-Migrate # (first time only, afterwards this should be in the Pipfile)
```

```sh
FLASK_APP=twitoff flask db init #> generates migrations dir
FLASK_APP=twitoff flask db migrate #> creates the db (with "alembic_version" table)
FLASK_APP=twitoff flask db upgrade #> creates tables in the db for each model
```

## Usage

```sh
FLASK_APP=twitoff flask run
```
