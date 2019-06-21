################################################################################
# Docker-compose django service commands for dev
################################################################################

run:
	docker-compose run django $(cmd)

flake8:
	docker-compose run django flake8

migrate:
	docker-compose run django python manage.py migrate $(app)

makemigrations:
	docker-compose run django python manage.py makemigrations

test:
	docker-compose run django python manage.py test $(app)

pytest:
	docker-compose run django pytest --disable-warnings -v $(app)

bash:
	docker-compose run django bash

shell:
	docker-compose run django python manage.py shell

coverage:
	docker-compose run django coverage run --source='.' manage.py test $(app)
	docker-compose run django coverage report

up:
	docker-compose up -d

logs:
	docker-compose logs -f

down:
	docker-compose down

build:
	docker-compose build

remove.volumes::
	docker-compose down
	docker volume rm integrati-api_postgres_data

clear.python:
	find . -type d -name __pycache__ -o \( -type f -name '*.py[co]' \) -print0 | xargs -0 rm -rf

clear.docker:
	docker ps | awk '{print $$1}' | grep -v CONTAINER | xargs docker stop
