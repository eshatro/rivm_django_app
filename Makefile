local-app-init: local-build start

# START pre build docker hub image
app-init: dh-build start

dh-build:
	docker pull enidoshatro/lab:rivm_api-latest
# END pre build docker hub image

# BEGIN local image build
local-build:
	docker build -t enidoshatro/lab:rivm_api-latest --rm .

start:
	docker compose up

shell:
	docker exec -it django /bin/bash

django-shell:
	docker exec -it django python manage.py shell

run-tests:
	docker exec -it django coverage run -m pytest --cov-report term --cov=rivm/graphql_rivm

remove-containers:
	docker compose down

flush-containers:
	docker compose down && docker volume rm graphql-api_local_postgres_data

tear-down:
	docker compose down && docker image rm enidoshatro/lab:rivm_api-latest postgres:11.6 && docker volume rm graphql-api_local_postgres_data
# END local image build
