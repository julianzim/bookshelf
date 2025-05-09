import os
from dotenv import load_dotenv

from pydantic import BaseModel, EmailStr
from fastapi_mail import ConnectionConfig

load_dotenv()


class AppConfig(BaseModel):
    APP_MODE: str = os.environ.get("APP_MODE")
    APP_LOG_LEVEL: str = os.environ.get("APP_LOG_LEVEL")
    APP_SECRET_AUTH: str = os.environ.get("APP_SECRET_AUTH")


class DatabaseConfig(BaseModel):
    DB_HOST: str = os.environ.get("DB_HOST")
    DB_PORT: int = os.environ.get("DB_PORT")
    DB_NAME: str = os.environ.get("DB_NAME")
    DB_USER: str = os.environ.get("DB_USER")
    DB_PASS: str = os.environ.get("DB_PASS")


class EmailConfig(BaseModel):
    MAIL_USERNAME: str = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD: str = os.environ.get("MAIL_PASSWORD")
    MAIL_FROM: EmailStr = os.environ.get("MAIL_FROM")
    MAIL_PORT: int = int(os.environ.get("MAIL_PORT"))  # 587 for TLS, 465 for SSL
    MAIL_SERVER: str = os.environ.get("MAIL_SERVER")
    MAIL_STARTTLS: bool = True
    MAIL_SSL_TLS: bool = False


app_config = AppConfig()
db_config = DatabaseConfig()
email_config = EmailConfig()

mail_conf = ConnectionConfig(
    MAIL_USERNAME=email_config.MAIL_USERNAME,
    MAIL_PASSWORD=email_config.MAIL_PASSWORD,
    MAIL_FROM=email_config.MAIL_FROM,
    MAIL_PORT=email_config.MAIL_PORT,
    MAIL_SERVER=email_config.MAIL_SERVER,
    MAIL_STARTTLS=email_config.MAIL_STARTTLS,
    MAIL_SSL_TLS=email_config.MAIL_SSL_TLS,
    USE_CREDENTIALS=True
)
