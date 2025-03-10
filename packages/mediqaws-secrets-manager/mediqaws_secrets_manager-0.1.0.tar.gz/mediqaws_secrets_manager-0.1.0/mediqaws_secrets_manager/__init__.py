import boto3
import json
import time

from botocore.exceptions import ClientError

class SecretsManager:
  def __init__(self, ttl: int = 3600):
    self.ttl = ttl # Cache time to live in seconds
    self.client = boto3.client("secretsmanager")
    self.cache = {}
    self.timestamps = {}

  def get_secret(self, secret_name: str) -> str:
    now = time.time()
    
    # Check if the secret is in the cache and if it is, return it
    if secret_name in self.cache and now - self.timestamps[secret_name] < self.ttl:
      return self.cache[secret_name]
    
    try:
      # Get the secret from AWS Secrets Manager
      response = self.client.get_secret_value(SecretId=secret_name)
      secret = response.get("SecretString") or response.get("SecretBinary")
      
      if isinstance(secret, str):
        try:
          secret = json.loads(secret)
        except json.JSONDecodeError:
          pass
      
      # Cache the secret
      self.cache[secret_name] = secret
      self.timestamps[secret_name] = now
      
      return secret
    except ClientError as e:
      raise Exception(f"Error getting secret {secret_name}: {e}")