import os

from mediqaws_secrets_manager import SecretsManager

def test_get_secret():
  secrets_manager = SecretsManager()

  secret = secrets_manager.get_secret(os.getenv("SECRET_NAME"))

  assert secret is not None
  print(secret)