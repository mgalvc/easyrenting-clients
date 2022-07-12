class InvalidDocumentException(Exception): 
  def __str__(self) -> str:
    return 'Invalid document number'