from datetime import date

import pytest
from tests.usecases.__mock__.client_repo import MockClientRepo
from tests.usecases.__mock__.mail_service import MockMailService
from usecases.dtos.client import ClientDTO
from usecases.exceptions.duplicated_document_number import DuplicatedDocumentNumber
from usecases.exceptions.duplicated_email import DuplicatedEmail
from usecases.register import register_client
from domain.exceptions.invalid_age import InvalidAgeException
from domain.exceptions.invalid_document import InvalidDocumentException

mail_service = MockMailService()

def test_register_client_success():
  repo = MockClientRepo()
  data = ClientDTO(name='Fulano', birthdate=date(1998, 8, 17), cpf='12894647077', email='fulano@email.com')
  client_id = register_client(data=data, mail_service=mail_service, repo=repo)
  assert client_id is not None
  assert repo.find(client_id) is not None

def test_register_invalid_age(): 
  repo = MockClientRepo()
  data = ClientDTO(name='Fulano', birthdate=date(2022, 8, 17), cpf='12894647077', email='fulano@email.com')
  with pytest.raises(InvalidAgeException):
    register_client(data=data, mail_service=mail_service, repo=repo)

def test_register_invalid_document():
  repo = MockClientRepo()
  data = ClientDTO(name='Fulano', birthdate=date(1998, 8, 17), cpf='12894647000', email='fulano@email.com')
  with pytest.raises(InvalidDocumentException):
    register_client(data=data, mail_service=mail_service, repo=repo)

def test_register_duplicated_document():
  repo = MockClientRepo()
  data_1 = ClientDTO(name='Fulano', birthdate=date(1998, 8, 17), cpf='12894647077', email='fulano@email.com')
  data_2 = ClientDTO(name='Fulano', birthdate=date(1998, 8, 17), cpf='12894647077', email='fulano2@email.com')
  register_client(data=data_1, mail_service=mail_service, repo=repo)
  with pytest.raises(DuplicatedDocumentNumber):
    register_client(data=data_2, mail_service=mail_service, repo=repo)

def test_register_duplicated_email(): 
  repo = MockClientRepo()
  data_1 = ClientDTO(name='Fulano', birthdate=date(1998, 8, 17), cpf='12894647077', email='fulano@email.com')
  data_2 = ClientDTO(name='Fulano', birthdate=date(1998, 8, 17), cpf='968.729.800-60', email='fulano@email.com')
  register_client(data=data_1, mail_service=mail_service, repo=repo)
  with pytest.raises(DuplicatedEmail):
    register_client(data=data_2, mail_service=mail_service, repo=repo)