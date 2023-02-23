from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone

# Create your models here.

class CustomManagerAccount(BaseUserManager):
    def create_superuser(self, email, username, first_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                "Superuser needs to set is_staff to true"
            )
        
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser needs to set is_superuser to true'
            )
        
        return self.create_user(email, username, first_name, password, **other_fields)
        

    
    def create_user(self, email, username, first_name, password, **other_fields):
        if not email:
            raise ValueError(
                "Email is required"
            )
        email = self.normalize_email(email)
        user = self.model(username = username, first_name = first_name,
                            email = email, password = password, **other_fields )
        user.set_password(password)
        user.save()
        return user



class NewUser(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(_('email address'), max_length = 255, unique = True)
    username = models.CharField(max_length = 255, unique = True)
    first_name = models.CharField(max_length = 255, blank = True)
    start_date = models.DateTimeField(default = timezone.now )
    about = models.TextField(_('About'), max_length = 255, blank = True)
    is_staff = models.BooleanField(default = False)
    is_active = models.BooleanField(default = False)

    objects = CustomManagerAccount()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name']

    def __str__(self):
        return self.username

