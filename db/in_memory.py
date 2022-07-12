from typing import List
from db.client_repo import IClientRepo
from domain.client import Client

clients: List[Client] = []

class InMemoryRepo(IClientRepo):

  def add(self, client):
    clients.append(client)

  def find(self, id):
    return next(iter([c for c in clients if c.id == id]), None)

  def find_by_cpf(self, cpf):
    return next(iter([c for c in clients if c.document_number == cpf]), None)

  def find_by_email(self, email):
    return next(iter([c for c in clients if c.email == email]), None)

  def update(self, client): pass