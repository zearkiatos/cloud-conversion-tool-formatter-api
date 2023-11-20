activate:
	source run.sh; activate

install:
	source run.sh; install

run:
	source run.sh; run $(port)

docker-up:
	source run.sh; docker_up

docker-down:
	source run.sh; docker_down

docker-pubsub-down:
	docker exec -it gcloud-pubsub-queue gcloud pubsub topics delete task-convert
	docker exec -it gcloud-pubsub-queue gcloud pubsub subscriptions delete task-convert-subscription

docker-dev-up:
	docker compose -f=docker-compose.develop.yml up --build

docker-dev-down:
	make docker-pubsub-down
	docker compose -f=docker-compose.develop.yml down

run-docker:
ifeq ($(strip $(port)),)
	flask run -h 0.0.0.0
else
	flask run -p $(port) -h 0.0.0.0
endif

run-worker:
	celery -A flaskr.tasks worker -l info

run-docker-worker:
ifeq ($(strip $(port)),)
	flask run -h 0.0.0.0; make run-worker
else
	flask run -p $(port) -h 0.0.0.0; make run-worker
endif

run-docker-gunicorn:
	gunicorn --bind 0.0.0.0:8000 wsgi:app; make run-worker


docker-gunicorn:
	gunicorn --bind 0.0.0.0:8000 wsgi:app