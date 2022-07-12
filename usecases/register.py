from datetime import datetime, timedelta, timezone

import jwt
from config.env import CONFIRMATION_BASE_URL, JWT_SECRET, SMTP_SENDER
from db.client_repo import IClientRepo
from domain.client import Client
from services.mail.mail_service import MailData, IMailService
from usecases.dtos.client import ClientDTO
from usecases.exceptions.duplicated_document_number import DuplicatedDocumentNumber
from usecases.exceptions.duplicated_email import DuplicatedEmail
from utils.mail import get_account_confirmation_message


def register_client(data: ClientDTO, mail_service: IMailService, repo: IClientRepo):
  client = Client(name=data.name, birthdate=data.birthdate, document_number=data.cpf, email=data.email)
  client.check_eligibility()

  same_cpf = repo.find_by_cpf(client.document_number)
  same_email = repo.find_by_email(client.email)

  if same_cpf: raise DuplicatedDocumentNumber()
  if same_email: raise DuplicatedEmail()

  token = jwt.encode({ 'ref': client.id, 'exp': datetime.now(tz=timezone.utc) + timedelta(seconds=90)}, JWT_SECRET, algorithm='HS256')
  confirmation_link = f'{CONFIRMATION_BASE_URL}/{token}'
  message = get_account_confirmation_message(client_name=client.name, confirmation_link=confirmation_link)
  mail_data = MailData(sender=SMTP_SENDER, receiver=client.email, message=message, subject='Welcome to EasyRenting')
  mail_service.send(data=mail_data)

  repo.add(client=client)
  return client.id