update:
	@pip install --upgrade pip

install:
	@pip install -r requirements.txt

install-dev: requirements-dev.txt
	@pip install -r requirements-dev.txt

run:
	@python manage.py run

test:
	@python -m pytest

build:
	@docker build -t ${imagename}:latest .

run-docker:
	@sudo docker run --env FLASK_ENV=development -p 5000:5000 ${imagename}:latest

pre-commit:
	@pre-commit install

initial-tag:
	@git tag -a -m "Initial tag." v0.0.1

bump-tag:
	@cz bump --check-consistency --changelog

initialize-db:
	@flask db init
	@flask db migrate -m "Initial Migration."
	@flask db upgrade

upgrade-db:
	@flask db upgrade

create-db:
	@python manage.py create_db

seed-db:
	@python manage.py seed_db

all: update install install-dev pre-commit initial-tag test create-db seed-db run
