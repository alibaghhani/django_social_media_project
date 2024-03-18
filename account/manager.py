from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self,username ,phone_number, password, **extra_fields):
        if not phone_number:
            raise ValueError('phone number must be set!')
        user = self.model(phone_number=phone_number,username=username,**extra_fields )
        user.set_password(password)
        user.save(using=self._db)
        return user





