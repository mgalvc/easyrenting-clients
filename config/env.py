from os import environ

from dotenv import load_dotenv

load_dotenv()

CONFIRMATION_BASE_URL = environ.get('CONFIRMATION_BASE_URL')

SMTP_USERNAME = environ.get('SMTP_USERNAME')
SMTP_PASSWORD = environ.get('SMTP_PASSWORD')
SMTP_HOST = environ.get('SMTP_HOST')
SMTP_PORT = environ.get('SMTP_PORT')
SMTP_SENDER = environ.get('SMTP_SENDER')

SQLITE_CONN_URL = environ.get('SQLITE_CONN_URL')

JWT_SECRET = environ.get('JWT_SECRET', 'secret')
