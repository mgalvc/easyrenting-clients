class DuplicatedEmail(Exception):
  def __str__(self) -> str:
    return "There's a client registered with this email address"