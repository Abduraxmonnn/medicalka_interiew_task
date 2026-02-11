# Django
from django.contrib.auth.base_user import BaseUserManager
from django.db.models.manager import BaseManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager, BaseManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        """
        Creates and saves a User with the given username, date of
        birth and password.
        """
        if not email:
            raise ValueError('The Email must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)

        if password:
            user.set_password(password)  # hashes password into password_hash
        else:
            raise ValueError("Password must be set")

        user.save(using=self._db)

        return user

    def create_admin(self, username, email=None, password=None, **extra_fields):
        """
        Creates and saves an admin with the given username and password.
        """
        extra_fields.setdefault('is_registered', True)
        extra_fields.setdefault('is_staff', True)

        if password is None:
            raise ValueError("Admin must have a password")

        return self.create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given username, date of
        birth and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username, email, password, **extra_fields)
