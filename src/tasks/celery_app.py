from celery import Celery
from src.config import app_config


app = Celery(
    "worker",
    broker=app_config.CELERY_BROKER_URL,
    backend=app_config.CELERY_RESULT_BACKEND,
    include=["src.tasks.email_tasks"],
    broker_connection_retry_on_startup=True
)

app.conf.update(
    task_always_eager=app_config.CELERY_DEV_MODE,
    task_eager_propagates=app_config.CELERY_DEV_MODE
)
