class ExpiredActivationToken(Exception):
  
  def __str__(self) -> str:
    return 'This activation token expired'