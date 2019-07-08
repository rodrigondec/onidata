# Onidata DRF Project
Project made with Django + PostgreSQL + DRF for Onidata interview

# Install
## Docker + docker-compose
Install [docker-ce](https://docs.docker.com/install/) and [docker-compose](https://docs.docker.com/compose/install/) from each documentation

### Setting up
On the project folder run the following commands:
1. `make config.env`
2. `make build`

# Running the project
Simply run the command `make up` and *voilà*

## Tests
On the project folder:
- run the command `make test` or `make test app=$(app_name)`. You may run the command `make coverage` instead.
- run the command `make flake8`
