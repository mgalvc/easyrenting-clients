from services.mail.mail_service import IMailService


class MockMailService(IMailService):
  def send(self, data):
    pass