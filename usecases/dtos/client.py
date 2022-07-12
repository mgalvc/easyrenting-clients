from dataclasses import dataclass
from datetime import date


@dataclass
class ClientDTO:
  name: str
  birthdate: date
  cpf: str
  email: str
