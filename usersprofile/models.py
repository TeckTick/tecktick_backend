from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
# Create your models here.
class CustomUserManager(BaseUserManager):
    """
    email is the unique identifier of the user
    """
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_("Email address is required"))
        if not password:
            raise ValueError(_("Password is required"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    """
    create and save a new user
    """ 
    # def create_user(self, email=None, password=None, **extra_fields):
    #     extra_fields.setdefault('is_staff', False)
    #     extra_fields.setdefault('is_superuser', False)
    #     return self._create_user(email, password, **extra_fields)

    """
    create and save a new superuser
    """    
    def create_superuser(self, email=None, password=None, **extra_fields):
        # extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff", False):
            raise ValueError(_("Superuser must have is_staff=True"))
        if extra_fields.get("is_superuser", False):
            raise ValueError(_("Superuser must have superuser=True"))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=80, unique=True)
    email = models.EmailField(max_length=80, unique=True)

    # extra fields 
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    phone = models.CharField(max_length=10, blank=True)
   
    is_staff = models.BooleanField(default=True)
    is_user = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = 'CustomUser'
        verbose_name_plural = 'CustomUsers'

    


