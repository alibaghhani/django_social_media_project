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

    def create_superuser(self,username,phone_number, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        user = self.create_user(username,phone_number, password, **extra_fields)
        user.save(using=self._db)
        if user.is_superuser:
            return user
        else:
            print('not super user')






