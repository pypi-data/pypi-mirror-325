# mediqaws-secrets-manager

AWS Secrets Manager with caching

## Installation

`pip install mediqaws-secrets-manager`

## Example

```python
from mediqaws_secrets_manager import SecretsManager

secrets_manager = SecretsManager()

secret = secrets_manager.get_secret("secret_name")
print(secret)
```
