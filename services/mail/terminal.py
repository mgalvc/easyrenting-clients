from services.mail.mail_service import IMailService


class TerminalService(IMailService):

  def send(self, data):
    print(data.message)