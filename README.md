# PodCity

PodCity is a simple web application that aggregates podcasts from various sources and _feeds_ them to you.
Inspiration comes from people who listen to multiple podcasts and want one place to access them all and also inspiration 
ideally just comes from apps like Apple Podcasts, Google Podcasts, Spotify and the likes.

This uses the [RSS](https://en.wikipedia.org/wiki/RSS_%28standard%29) standard to aggregate the feeds as most feeds 
follow this standard, making the aggregation process simpler.

## Pre-requisites

Some few requirements before you can use PodCity:

### Docker and Docker Compose

Docker is being used to run the web application and the database. In this case however, all you will need to use it for
is to run the database.

Ensure you have docker installed and that you have docker-compose installed as well. Check [here](https://www.docker.com/)
and [here](https://docs.docker.com/compose/) for more information.

This is not a hard requirement, but you can also use [Postgres](https://www.postgresql.org/) locally installed to
run the database. If you prefer to change the database engine, like [MySQL](https://www.mysql.com/), then more code
changes will need to be made.

### Python 3+, Pip and Virtualenv

This application runs on Python 3+, so make sure you have Python 3+ installed in you local development machine. Check 
[here](https://www.python.org/downloads/) for more information. Also, you will need [Pip](https://pypi.org/project/pip/)
and [virtualenv](https://virtualenv.pypa.io/) installed.

## Getting Started

Getting started is quite simple and requires few steps to get started.

After cloning the repository, you will need to run the following commands in the root directory of the repository:

```bash
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

> Sets up virtualenv for the project and installs the dependencies.

Set up the environment variables for the application:

```bash
cp .env.sample .env
```

> After this, you can change the values in the .env file to your liking.

Now you can run the database with docker compose(if you have it installed and if this is the preferred way for running
the database).

```bash
docker-compose up
```

> if on linux
 

```bash
docker compose up
```

> If running on MacOS

## Running Tests

Running tests is quite simple and is a matter or running the following command:

```bash
python manage.py test
```

## Running the Application

Now, for the fun part, running the application. Running the application requires the following steps:

```bash
python manage.py makemigrations 
python manage.py migrate
```

> First run migrations to ensure that the database is up-to date.
 
```bash
python manage.py createsuperuser
```

> Create a super-user to be able to access Admin panel. Follow the prompts from the command line.

Next step is to run the commands to fetch podcasts and feed them into the database. This can be done
as below:

```bash
python manage.py feedjob
```

> This command will fetch the podcasts and feed them into the database. Checkout more of the code [here](./podcasts/management/commands/feedjob.py)
 
Now, you can run the application with the following command:

```bash
python manage.py runserver
```

You can now be able to access the Admin Panel [here](http://localhost:8000/admin) and the application [here](http://localhost:8000/).

That's it! You should now be able to use PodCity to aggregate podcasts from various sources and feed them to you.

Adding more podcasts is as simple as adding them to [Feed Job](./podcasts/management/commands/feedjob.py). 

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags](https://github.com/SanctumLabs/podcity/releases) 
in this repository.

## Built With

- [Django](https://www.djangoproject.com/)
- [Python](https://www.python.org/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Postgres](https://www.postgresql.org/)
- [Pip](https://pypi.org/project/pip/)
- [Virtualenv](https://virtualenv.pypa.io/)
- [Django AP Scheduler](https://github.com/jcass77/django-apscheduler)
- [Feed Parser](https://pythonhosted.org/feedparser/)
- [Django Environ](https://django-environ.readthedocs.io/)

## Authors

- [Lusina](https://github.com/BrianLusina) -  Initial Work

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details

![forthebadge](./docs/images/built-with-python.svg)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
