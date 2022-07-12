class ClientNotFound(Exception):

  def __str__(self) -> str:
    return 'Client not found'