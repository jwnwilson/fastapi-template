build:
	docker-compose build --build-arg INSTALL_DEV=true

run:
	docker-compose up

stop:
	docker-compose down

test:
	docker-compose run api pytest

lint:
	docker-compose run api bash -c "../scripts/lint.sh"

static-check:
	docker-compose run api bash -c "../scripts/lint.sh -check"

clean:
	rm **/**/*.pyc
	rm **/**/__pycache__