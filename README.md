# Talana Django Backend Engineer Technical Test

This is a technical test for the Talana company for the position of Backend
Engineer.

## Development Server

This solution was built in a development environment provided by the Vagrant
box ubuntu/bionic64, which is the official Ubuntu 18.04 LTS (Bionic Beaver)
builds.

To replicate this environment you need to run `vagrant up --provision`

**IMPORTANT!**
Make sure ports 8000 (Django Development Server), 5432 (PostgreSQL) and 5555
(Flower Monitoring) are available in your system. Also, the `--provision` flag
important to apply the necessary settings to the development environment, this
are specified in the Vagrant file provided in the source code.

Then run the `vagrant ssh` command to access the recently created Ubuntu machine

## Available Scripts

Once you have completed the previous steps, in the project directory you can run:

### Build

Run `sudo docker-compose build` to build or rebuild the services.

### Run the app in development mode

Run `sudo docker-compose up` to builds, (re)creates, starts, and attaches to
containers for a service. Then go to [http://localhost:8000](http://localhost:8000)
to view it in your favorite browser.

### Running unit tests

Run `sudo docker-compose run --rm app sh -c "python manage.py test && flake8"` to
execute the unit tests and linting the source code with flake8, verifying pep8,
pyflakes and circular complexity.

### Run the app in production mode

Run `sudo docker-compose up -d --build` to first make your services builds and then,
to start the containers in the background and leave them running.

If you have already built them just run `sudo docker-compose up -d`

## Technologies involved

- Redis
- Docker
- Python
- Django
- Travis CI
- PostgreSQL
- Django Rest Framework
- Celery: Distributed Task Queue
