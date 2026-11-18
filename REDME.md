# working_with_celery

A small learning project for running background tasks in a Django project with Celery. It uses Redis as the message broker and Docker Compose to run everything together.

## What I learned

- **Docker and Docker Compose**: building images, defining services, mapping ports and volumes
- **Celery**: defining tasks, running a worker, and loading config from Django settings
- **Redis**: using it as the broker that passes tasks from Django to the Celery worker

## How it works

1. Django (or a shell command) calls a task with `.delay()`.
2. The task is placed on a queue in Redis.
3. A Celery worker picks it up and runs it in the background.

## Tech stack

- Python 3.11
- Django
- Celery
- Redis
- Docker / Docker Compose

## Project structure

```
.
├── docker-compose.yml
├── working_with_celery/
│   ├── settings.py
│   ├── celery.py        # Celery app and task discovery
│   ├── __init__.py      # loads the Celery app when Django starts
│   └── ...
└── requirements.txt
```

## Getting started

### Prerequisites

- Docker and Docker Compose installed

### Run the project

```bash
docker-compose up -d --build
```

The Django app is available at http://localhost:8001.

### Check that the worker is running

```bash
docker-compose logs -f celery
```

(Replace `celery` with the name of your worker service in `docker-compose.yml`.)

### Try a task

Open a Django shell inside the container:

```bash
docker-compose exec django python manage.py shell
```

Then call the sample task:

```python
from working_with_celery.celery import add_number
add_number.delay(2, 3)
```

The result should appear in the worker logs.

## Configuration

Celery settings live in `settings.py` and use the `CELERY_` prefix, for example:

```python
CELERY_BROKER_URL = "redis://redis:6379/0"
```

The host `redis` is the service name from `docker-compose.yml`, not `localhost`.

## Issues I ran into

- **`invalid mount path` / invalid compose file**: volumes and ports must be YAML lists, and container paths must be absolute (`/usr/src/app`).
- **`'celery' object has no attribute 'config'`**: the correct method is `app.config_from_object(...)`.
- **`No module named 'packaging'`**: the Redis transport needs it, so I added it to `requirements.txt` (or install `celery[redis]`).
