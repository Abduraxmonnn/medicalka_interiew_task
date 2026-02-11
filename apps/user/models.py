# Python
import uuid

# Django
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.password_validation import validate_password
from django.core.validators import MinLengthValidator

# Project
from apps.user.manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, validators=[MinLengthValidator(3)])
    full_name = models.CharField(max_length=100, validators=[MinLengthValidator(3)])

    password_hash = models.CharField(max_length=128)

    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def set_password(self, raw_password):
        """
        Hashes the password and stores it in password_hash with full Django validation.
        """
        # Validate password
        validate_password(raw_password, self)
        # Hash password
        self.password_hash = make_password(raw_password)

    def check_password(self, raw_password):
        """
        Check the raw password against the hashed password.
        """
        return check_password(raw_password, self.password_hash)

    def __str__(self):
        return self.email
