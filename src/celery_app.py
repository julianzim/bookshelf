from celery import Celery
from kombu import Queue
from src.config import app_config


app = Celery(
    "worker",
    broker=app_config.CELERY_BROKER_URL,
    backend=app_config.CELERY_RESULT_BACKEND,
    include=["src.tasks"],
    broker_connection_retry_on_startup=True
)

app.conf.update(
    task_always_eager=app_config.CELERY_DEV_MODE,
    task_eager_propagates=app_config.CELERY_DEV_MODE,
    worker_concurrency=16,
    task_acks_late=True,
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    task_default_queue="default",
    task_queues = [
        Queue("default"),
        Queue("email"),
    ],
)
