setup:
	docker-compose build

run:
	docker-compose up

stop:
	docker-compose down

test:
	docker-compose run api mvn test

reset-db: stop
	docker volume rm aktion_api_data