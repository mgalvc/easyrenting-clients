class DuplicatedDocumentNumber(Exception):
  def __str__(self) -> str:
    return "There's a client registered with this document number"