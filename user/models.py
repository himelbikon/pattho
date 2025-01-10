from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError('User must have an email!')
        if not password:
            raise ValueError('User must have an password!')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.is_staff = False
        user.is_superuser = False
        user.is_active = True
        user.is_email_verified = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError('User must have an email!')
        if not password:
            raise ValueError('User must have an password!')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.is_email_verified = False
        user.save(using=self._db)
        return user


class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)

    image = models.ImageField(blank=True, null=True, upload_to='images/user')

    created_at = models.DateField(auto_now_add=True)

    is_email_verified = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    two_factor_auth = models.BooleanField(default=False)

    class Meta:
        ordering = ['-id']

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return f'{self.id}. {self.email}'


    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'
