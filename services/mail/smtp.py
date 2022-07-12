from email.mime.text import MIMEText
import smtplib

from services.mail.mail_service import IMailService


class SMTPService(IMailService):

  def __init__(self, username: str, password: str, host: str, port: int):
    self.__username = username
    self.__password = password
    self.__host = host
    self.__port = port

  def send(self, data):
    message = MIMEText(data.message, 'html')
    message["Subject"] = data.subject
    message["From"] = data.sender
    message["To"] = data.receiver
    
    with smtplib.SMTP(self.__host, self.__port) as server:
      server.ehlo()
      server.starttls()
      server.login(self.__username, self.__password)
      server.sendmail(data.sender, data.receiver, message.as_string())