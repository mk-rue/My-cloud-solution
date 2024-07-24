from django.db import models # type: ignore
from cryptography.fernet import Fernet # type: ignore
import base64

class EncryptedField(models.CharField):
    def __init__(self, *args, **kwargs):
        self.key = base64.urlsafe_b64decode(b'your_base64_encoded_key_here')
        super(EncryptedField, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        if value:
            cipher_suite = Fernet(self.key)
            value = cipher_suite.encrypt(value.encode())
        return value

    def from_db_value(self, value, expression, connection):
        if value:
            cipher_suite = Fernet(self.key)
            value = cipher_suite.decrypt(value).decode()
        return value

class Company(models.Model):
    name = EncryptedField(max_length=255)
    registration_date = models.DateField()
    # other fields...
