lint:
	flake8 app

build:
	sudo docker-compose build

run_app:
	sudo docker-compose up -d