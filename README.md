# Onidata DRF Project
Project made with Django + PostgreSQL + DRF for Onidata interview

# Install
## Docker + docker-compose
Install [docker-ce](https://docs.docker.com/install/) and [docker-compose](https://docs.docker.com/compose/install/) from each documentation

### Setting up
On the project folder run the following commands:
1. `$ make config.env` to copy the file `.env.example` to `.env`
2. `$ make build` to build docker containers

# Running the project
Simply run the command `$ make up` and *voilà*.

This command will start 3 services on your machine:
- Django server on [http://0.0.0.0:8000](http://0.0.0.0:8000)
- PgAdmin server on [http://0.0.0.0:5050](http://0.0.0.0:5050)
- PostgreSQL service on port [5432]()

## Tests
On the project folder:
- run the command `$ make test` or `$ make test app=$(app_name)`. You may run the command `$ make coverage` instead.
- run the command `$ make flake8`

## Administration
Django Admin Site is enabled for the project on [http://0.0.0.0:8000/admin](http://0.0.0.0:8000/admin).

The command `$ make populate.superuser` may be used to create the superuser `User(username='superuser', password='@Admin123')`.

## Using the API
Access the [localhost server](http://0.0.0.0:8000) and browse the api. 
> DRF Coreapi Documentation 
![coreapi documentation](docs/coreapi.png?raw=true "Coreapi Documentation")

You may interact with the API via browser or via http request softwares such as [Insomnia](#insomnia-setup)

### Authentication
`BasicAuthentication`, `SessionAuthentication` and `JWTAuthentication` are enabled on the API.

### JWTAuthentication
Pass the token following the curl example. If there's some confusion about JWT read about it on [JWT Oficial Documentation](https://jwt.io/) or the lib [drf-simplejwt](https://github.com/davesque/django-rest-framework-simplejwt)
```bash
curl \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiY29sZF9zdHVmZiI6IuKYgyIsImV4cCI6MTIzNDU2LCJqdGkiOiJmZDJmOWQ1ZTFhN2M0MmU4OTQ5MzVlMzYyYmNhOGJjYSJ9.NHlztMGER7UADHZJlxNG0WSi22a2KaYSfd1S-AuT7lU" \
  http://localhost:8000/api/some-protected-view/
```

### Insomnia Setup
Install Insomnia Rest from the [official website](https://insomnia.rest/download/).

Import the file `insomnia_data.json` located on the project folder.
> import file
![insomnia import](docs/insomnia_import.png?raw=true "Insomnia Import")

Activate the `Onidata` workspace and `Onidata` environment
> workpsace
![onidata workspace](docs/onidata_workspace.png?raw=true "Onidata Workspace")

> enviroment
![onidata environment](docs/onidata_environment.png?raw=true "Onidata Environment")

## Major libs used
- [Django](https://www.djangoproject.com/)
- [DRF](https://www.django-rest-framework.org/)
- [Coreapi](https://www.coreapi.org/)
- [drf-simplejwt](https://github.com/davesque/django-rest-framework-simplejwt)
- [factory boy](https://factoryboy.readthedocs.io/en/latest/)
- [pendulum](https://pendulum.eustace.io/)
