import jwt
from config.env import JWT_SECRET
from db.client_repo import IClientRepo
from usecases.exceptions.client_not_found import ClientNotFound
from usecases.exceptions.expired_activation_token import ExpiredActivationToken


def activate_account(token: str, repo: IClientRepo):
  try:
    payload = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
    client = repo.find(payload['ref'])
    if not client: raise ClientNotFound()
    client.activate()
    repo.update(client)
  except jwt.ExpiredSignatureError:
    raise ExpiredActivationToken()