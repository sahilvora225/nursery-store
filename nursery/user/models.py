from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin

# Create your models here.

class UserManager(BaseUserManager):
    """
    Manager for User model.
    """
    def create_user(self, email, password, *args, **kwargs):
        if not email:
            return ValueError('Email Field is compulsory')
        user = self.model(email=self.normalize_email(email), *args, **kwargs)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, *args, **kwargs):
        user = self.create_user(email, password, *args, **kwargs)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    User Model.
    """
    USER_TYPE_CHOICES = (('S', 'Seller'), ('B', 'Buyer'))
    name = models.CharField(max_length=254)
    email = models.EmailField(unique=True, max_length=254)
    user_type = models.CharField(max_length=2, choices=USER_TYPE_CHOICES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'