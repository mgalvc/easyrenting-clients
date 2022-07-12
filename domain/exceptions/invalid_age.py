class InvalidAgeException(Exception):
  def __str__(self) -> str:
    return 'You need to be at least 18 years old'