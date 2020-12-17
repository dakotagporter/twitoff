# Deployment Guide

## Prerequisites

  + [Heroku CLI](https://devcenter.heroku.com/articles/getting-started-with-python?singlepage=true) (after installing the CLI, also perform a `heroku login`)

## Preparations

Install production dependencies:

```sh
pipenv install gunicorn psycopg2-binary
```

Make a Procfile and place the following inside:

    web: gunicorn twitoff:APP -t 120

## Server Management

Create the server:

```sh
heroku create twitoff-21 # you'll need to choose your own name instead of twitoff-21
```

Configure the server:

```sh
heroku config:set ENV="production"
heroku config:set FLASK_ENV="production"
heroku config:set TWITTER_API_KEY="______________"
heroku config:set TWITTER_API_KEY_SECRET="__________"
```

## Deploying

Deploy:

```sh
git push heroku main
# git push heroku my-branch:main
```

> NOTE: if you are seeing an error on the package installation step (ModuleNotFoundError: No module named 'Cython'), as a fallback, you can try using a requirements.txt approach instead of the Pipfile:
> `pipenv lock --requirements > requirements.txt`


## Database Management

Provision the database:

```sh
heroku addons:create heroku-postgresql:hobby-dev
```

Migrate the database (need to deploy first, to reference our app code):

```sh
# login to the server:
heroku run bash
FLASK_APP=twitoff flask db init #> generates app/migrations dir
FLASK_APP=twitoff flask db migrate #> creates the db (with "alembic_version" table)
FLASK_APP=twitoff flask db upgrade #> creates the specified tables
# then "exit" the server
```

## Viewing

```sh
heroku open
```

## Logs

```sh
heroku logs --tail
```



Errs:

"psycopg2.errors.StringDataRightTruncation: value too long for type character varying(300)"
