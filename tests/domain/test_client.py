from datetime import date

import pytest
from domain.client import Client, Status
from domain.exceptions.invalid_age import InvalidAgeException
from domain.exceptions.invalid_document import InvalidDocumentException


def test_client_is_eligible():
  client = Client(name='Matheus', birthdate=date(year=1998, month=8, day=17), document_number='128.946.470-77', email='matheus@email.com')
  assert client.check_eligibility() == True

def test_client_has_invalid_age():
  client = Client(name='Matheus', birthdate=date(year=2022, month=8, day=17), document_number='128.946.470-77', email='matheus@email.com')
  with pytest.raises(InvalidAgeException):
    client.check_eligibility()

def test_client_has_invalid_document():
  client = Client(name='Matheus', birthdate=date(year=1998, month=8, day=17), document_number='128.946.470-00', email='matheus@email.com')
  with pytest.raises(InvalidDocumentException):
    client.check_eligibility()

def test_client_has_unique_id():
  ids = [Client(name='Matheus', birthdate=date(year=1998, month=8, day=17), document_number='128.946.470-77', email='matheus@email.com').id for i in range(10)]
  ids_set = set(ids)
  assert len(ids) == len(ids_set)

def test_client_created_as_registered():
  client = Client(name='Matheus', birthdate=date(year=1998, month=8, day=17), document_number='128.946.470-77', email='matheus@email.com')
  assert client.status == Status.REGISTERED

def test_client_activates():
  client = Client(name='Matheus', birthdate=date(year=1998, month=8, day=17), document_number='128.946.470-77', email='matheus@email.com')
  client.activate()
  assert client.status == Status.ACTIVATED



