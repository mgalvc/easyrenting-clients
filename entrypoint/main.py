from datetime import date
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from config.env import SMTP_HOST, SMTP_PASSWORD, SMTP_PORT, SMTP_USERNAME, SQLITE_CONN_URL
from db.sqlalchemy import SQLAlchemyRepo

from domain.exceptions.invalid_age import InvalidAgeException
from domain.exceptions.invalid_document import InvalidDocumentException
from services.mail.smtp import SMTPService
from services.mail.terminal import TerminalService
from usecases.activate_client import activate_account
from usecases.dtos.client import ClientDTO
from usecases.exceptions.client_not_found import ClientNotFound
from usecases.exceptions.duplicated_document_number import DuplicatedDocumentNumber
from usecases.exceptions.duplicated_email import DuplicatedEmail
from usecases.exceptions.expired_activation_token import ExpiredActivationToken
from usecases.get_all import get_all_clients
from usecases.register import register_client


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ClientData(BaseModel):
  name: str
  birthdate: date
  cpf: str
  email: str

@app.get('/healthcheck')
def healthcheck():
  return { 'healthy': True }

@app.post('/register')
async def register(body: ClientData):
  client_data = ClientDTO(name=body.name, birthdate=body.birthdate, cpf=body.cpf, email=body.email)
  # mail_service = TerminalService()
  mail_service = SMTPService(username=SMTP_USERNAME, password=SMTP_PASSWORD, host=SMTP_HOST, port=SMTP_PORT)
  repo = SQLAlchemyRepo(SQLITE_CONN_URL)
  
  try:
    client_id = register_client(data=client_data, mail_service=mail_service, repo=repo)
    return { 'id': client_id }
  except (InvalidDocumentException, InvalidAgeException) as error:
    raise HTTPException(status_code=422, detail=str(error))
  except (DuplicatedDocumentNumber, DuplicatedEmail) as error:
    raise HTTPException(status_code=409, detail=str(error))

@app.get('/confirm-account/{token}')
def confirm_account(token: str):
  repo = SQLAlchemyRepo(SQLITE_CONN_URL)

  try:
    activate_account(token, repo=repo)
    return { 'success': True }
  except ExpiredActivationToken as error:
    raise HTTPException(status_code=403, detail=str(error))
  except ClientNotFound as error:
    raise HTTPException(status_code=404, detail=str(error))

@app.get('/clients')
def get_all():
  repo = SQLAlchemyRepo(SQLITE_CONN_URL)
  clients = get_all_clients(repo=repo)
  return clients

  