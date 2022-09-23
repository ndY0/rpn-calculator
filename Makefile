include .env


init:
	cp .env.dist .env
	cp ./project/.env.dist ./project/.env

images:
	docker build . --build-arg FLASK_RUN_HOST --build-arg FLASK_APP --build-arg FLASK_ENV

start:
	docker-compose up

stop:
	docker-compose down

clean: stop
	docker container prune