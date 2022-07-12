from db.client_repo import IClientRepo


def get_all_clients(repo: IClientRepo):
  return [{
    'id': c.id,
    'name': c.name,
    'birthdate': c.birthdate,
    'cpf': c.document_number,
    'email': c.email,
    'status': c.status.name
  } for c in repo.get_all()]