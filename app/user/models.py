from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """Manager for user profile"""

    def create_user(self, email, password=None, **extra_fields):
        """Create a user profile"""
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)  # Ensure password being encrypted
        user.save(using=self._db)  # Save objects in django

        return user

    def create_superuser(self, email, password):
        """Create a user profile"""
        user = self.create_user(email, password)

        user.is_superuser = True  # 'is_superuser' is created automatically
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Database model for user in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    telephone = models.CharField(max_length=255, blank=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_available = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    requests = models.ManyToManyField(
        'car.Car',
        through='Request',
        through_fields=('user', 'car'),
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # For the superuser

    def get_full_name(self):
        """Retrieve full name of the user"""
        return self.name+self.last_name

    def get_short_name(self):
        """Retrieve short name of the user"""
        return self.name

    def __str__(self):
        """Retrieve String representation of our user"""
        return self.email


class Request(models.Model):
    """Database model for Request in the system"""
    PENDING = 'PE'
    APPROVED = 'AD'
    REJECTED = 'RE'
    STATE_CHOICES = [
        (PENDING, 'Pendiente'),
        (APPROVED, 'Aprobado'),
        (REJECTED, 'Rechazado')
    ]
    state = models.CharField(max_length=2,
                             choices=STATE_CHOICES,
                             blank=True,
                             default=PENDING)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             blank=False)
    car = models.ForeignKey('car.Car',
                            on_delete=models.CASCADE,
                            blank=False)
    retirement_date = models.DateTimeField(blank=False, null=True)
    return_date = models.DateTimeField(blank=False, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
