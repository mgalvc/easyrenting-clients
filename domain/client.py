from datetime import date
from enum import Enum
from typing import Optional
import uuid
from dateutil.relativedelta import relativedelta
from domain.exceptions.invalid_age import InvalidAgeException
from domain.exceptions.invalid_document import InvalidDocumentException

from utils.validate_cpf import validate_cpf


class Status(Enum):
	REGISTERED = 1
	ACTIVATED = 2

class Client:

	def __init__(self, name: str, birthdate: date, document_number: str, email: str, id: Optional[str] = None, status: Optional[Status] = Status.REGISTERED) -> None:
		self.__name = name
		self.__birthdate = birthdate
		self.__document_number = document_number
		self.__email = email
		self.__id = id or str(uuid.uuid4())
		self.__status = status

	@property
	def age(self) -> int:
		today = date.today()
		return relativedelta(today, self.__birthdate).years

	@property
	def email(self):
		return self.__email

	@property
	def name(self):
		return self.__name

	@property
	def birthdate(self):
		return self.__birthdate

	@property
	def document_number(self):
		return self.__document_number

	@property
	def email(self):
		return self.__email

	@property
	def id(self):
		return self.__id

	@property
	def status(self):
		return self.__status

	def check_eligibility(self) -> bool:
		if self.age < 18: raise InvalidAgeException()
		if not validate_cpf(self.__document_number): raise InvalidDocumentException()
		return True

	def activate(self) -> None:
		self.__status = Status.ACTIVATED