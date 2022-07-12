from abc import ABC, abstractmethod
from typing import List

from domain.client import Client


class IClientRepo(ABC):

  @abstractmethod
  def add(self, client: Client) -> None: pass

  @abstractmethod
  def find(self, id: str) -> Client: pass

  @abstractmethod
  def find_by_cpf(self, cpf: str) -> Client: pass

  @abstractmethod
  def find_by_email(self, email: str) -> Client: pass

  @abstractmethod
  def update(self, client: Client) -> None: pass

  @abstractmethod
  def get_all(self) -> List[Client]: pass