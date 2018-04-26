from django.db import models
#substituing a custom user model to override django's standard user model
from django.contrib.auth.models import AbstractBaseUser
#PermissionsMixin allows us to add permissions on the user model
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


# Create your models here.

class UserProfileManager(BaseUserManager):
    """Helps Django work with out custom user model."""

    def create_user(self, email, name, password=None):
        """Creates a new user profile object."""
        if not email:
            raise ValueError('Users must have an email address.')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        #django's set password will encrypt the password
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Creates and saves a new super user with given details."""

        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represent a "user profile" inside our system."""

#the parameter automatically generate a validation.
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

#helper class to make django override the user model with out custom user model
    objects = UserProfileManager()
#the standard django user model has the username field, replace it with email
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']


    def get_full_name(self):
        """Used to get a users full name."""

        return self.name

    def get_short_name(self):
        """Used to get a users short name."""

        return self.name

    def __str__(self):
        """Django uses this method to convert the object to a string"""

        return self.email


