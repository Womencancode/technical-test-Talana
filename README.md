# Talana Django Backend Engineer Technical Test

This is a technical test for the Talana company for the position of Backend Engineer

## Available Scripts

In the project directory, you can run:

### Build

Run `docker-compose build` to build or rebuild the services.

### Run the app in development mode

Run `docker-compose up` to builds, (re)creates, starts, and attaches to
containers for a service. Then go to [http://localhost:8000](http://localhost:8000)
to view it in your favorite browser.

### Running unit tests

Run `docker-compose run --rm app sh -c "python manage.py test && flake8"` to
execute the unit tests and linting the source code with flake8, verifying pep8,
pyflakes and circular complexity.

### Run the app in production mode

Run `docker-compose up -d --build` to first make your services builds and then,
to start the containers in the background and leave them running.

If you have already built them just run `docker-compose up -d`

## Technologies involved

- Redis
- Docker
- Python
- Django
- Travis CI
- PostgreSQL
- Django Rest Framework
- Celery: Distributed Task Queue
