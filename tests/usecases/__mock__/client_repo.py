from typing import List
from db.client_repo import IClientRepo


class MockClientRepo(IClientRepo):

  def __init__(self) -> None:
    self.clients = []

  def add(self, client):
    self.clients.append(client)

  def find(self, id):
    return next(iter([c for c in self.clients if c.id == id]), None)

  def find_by_cpf(self, cpf):
    return next(iter([c for c in self.clients if c.document_number == cpf]), None)

  def find_by_email(self, email):
    return next(iter([c for c in self.clients if c.email == email]), None)

  def update(self, client): pass

  def get_all(self):
    return self.clients