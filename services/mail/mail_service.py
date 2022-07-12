from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass(frozen=True)
class MailData:
  sender: str
  receiver: str
  message: str
  subject: str


class IMailService(ABC):
  @abstractmethod
  def send(self, data: MailData): pass