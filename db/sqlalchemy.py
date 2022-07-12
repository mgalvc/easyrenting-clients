from datetime import date, datetime
from typing import List
from sqlalchemy import create_engine, text
from db.client_repo import IClientRepo
from domain.client import Client, Status

class SQLAlchemyRepo(IClientRepo):

  def __init__(self, url: str) -> None:
    self.engine = create_engine(url, echo=True, future=True)

  def add(self, client) -> None:
    with self.engine.connect() as conn:
      statement = '''
        INSERT INTO clients (uuid, name, birthdate, document_number, email, status) 
        VALUES (:uuid, :name, :birthdate, :document_number, :email, :status)
      '''
      conn.execute(
        text(statement), 
        [{
          'uuid': client.id,
          'name': client.name,
          'birthdate': client.birthdate.strftime('%Y-%m-%d'),
          'document_number': client.document_number,
          'email': client.email,
          'status': client.status.value}])
      conn.commit()

  def find(self, id: str) -> Client:
    with self.engine.connect() as conn:
      statement = 'SELECT * FROM clients WHERE uuid = :uuid'
      result = conn.execute(text(statement), { 'uuid': id })
      result_list = [r for r in result.mappings()]
      client = next(iter(result_list), None)
      if not client: return None
      return Client(
        id=client.uuid, 
        name=client.name, 
        birthdate=datetime.strptime(client.birthdate, '%Y-%m-%d').date(), 
        document_number=client.document_number, 
        email=client.email, 
        status=Status(client.status))
      

  def find_by_cpf(self, cpf: str) -> Client:
    with self.engine.connect() as conn:
      statement = 'SELECT * FROM clients WHERE document_number = :cpf'
      result = conn.execute(text(statement), { 'cpf': cpf })
      result_list = [r for r in result.mappings()]
      client = next(iter(result_list), None)
      if not client: return None
      return Client(
        id=client.uuid, 
        name=client.name, 
        birthdate=datetime.strptime(client.birthdate, '%Y-%m-%d').date(), 
        document_number=client.document_number, 
        email=client.email, 
        status=Status(client.status))

  def find_by_email(self, email: str) -> Client:
    with self.engine.connect() as conn:
      statement = 'SELECT * FROM clients WHERE email = :email'
      result = conn.execute(text(statement), { 'email': email })
      result_list = [r for r in result.mappings()]
      client = next(iter(result_list), None)
      if not client: return None
      return Client(
        id=client.uuid, 
        name=client.name, 
        birthdate=datetime.strptime(client.birthdate, '%Y-%m-%d').date(), 
        document_number=client.document_number, 
        email=client.email, 
        status=Status(client.status))

  def update(self, client: Client) -> None:
    with self.engine.connect() as conn:
      statement = '''
        UPDATE clients SET 
          name = :name, 
          birthdate = :birthdate, 
          document_number = :document_number, 
          email = :email, 
          status = :status
        WHERE uuid = :uuid 
      '''
      conn.execute(
        text(statement), 
        [{
          'uuid': client.id,
          'name': client.name,
          'birthdate': client.birthdate.strftime('%Y-%m-%d'),
          'document_number': client.document_number,
          'email': client.email,
          'status': client.status.value}])
      conn.commit()

  def get_all(self) -> List[Client]:
    with self.engine.connect() as conn:
      statement = 'SELECT * FROM clients'
      result = conn.execute(text(statement))
      result_list = [r for r in result.mappings()]
      clients = []
      for r in result_list:
        clients.append(Client(
          id=r.uuid, 
          name=r.name, 
          birthdate=datetime.strptime(r.birthdate, '%Y-%m-%d').date(), 
          document_number=r.document_number, 
          email=r.email, 
          status=Status(r.status)))
      return clients
