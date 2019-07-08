# Onidata DRF Project
Project made with Django + PostgreSQL + DRF for Onidata interview

# Install
## Docker + docker-compose
Install [docker-ce](https://docs.docker.com/install/) and [docker-compose](https://docs.docker.com/compose/install/) from each documentation

### Setting up
On the project folder run the following commands:
1. `$ make config.env`
2. `$ make build`

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

# Using the API
Access the [localhost server](http://0.0.0.0:8000) and browse the api. 
> DRF Coreapi Documentation 
![coreapi documentation](docs/coreapi.png?raw=true "Coreapi Documentation")

You may interact with the API via browser or via http request softwares such as [Insomnia](#insomnia-setup)

## Insomnia Setup
Install Insomnia Rest from the [official website](https://insomnia.rest/download/).

Import the file `insomnia_data.json` located on the project folder.
> import file
![insomnia import](docs/insomnia_import.png?raw=true "Insomnia Import")

Activate the `Onidata` workspace and `Onidata` environment
> workpsace
![onidata workspace](docs/onidata_workspace.png?raw=true "Onidata Workspace")

> enviroment
![onidata environment](docs/onidata_environment.png?raw=true "Onidata Environment")
