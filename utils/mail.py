def get_account_confirmation_message(client_name: str, confirmation_link: str):
  return f'''

<p>Hey {client_name},</p>

<p>Be welcome to our platform. Follow the link below to confirm your account:</p>

<a href="{confirmation_link}">Confirmation link</a>

  '''