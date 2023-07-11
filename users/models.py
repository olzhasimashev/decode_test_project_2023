from django.core.mail import send_mail
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator

from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self, email, username, full_name, password, **extra_fields):

        if not email:
            raise ValueError('The given email must be set')
        if not username:
            raise ValueError('The given username must be set')
        if not full_name:
            raise ValueError('The given full name must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(
            email=email, username=username, full_name=full_name,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, username, full_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(
            email, username, full_name, password, **extra_fields
        )
    def create_superuser(self, email, username, full_name, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(
            email, username, full_name, password, **extra_fields
        )



class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[username_validator],
        verbose_name='Логин'
    )
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255, verbose_name='ФИО', blank=False, )
    birthday = models.DateField(
        null=True,
        blank=True
    )
    profile_avatar = models.ImageField(verbose_name='Фото профиля', blank=True, upload_to="photos/%Y/%m/%d/",default='photos/default_profile.png')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    creadit_card = models.CharField(verbose_name='Банковская карта', max_length=16, validators=[MinLengthValidator(16)])

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'full_name']
    objects = UserManager()
    def str(self):
        return self.email
    def get_short_name(self):
        return self.email
    def get_full_name(self):
        return self.full_name
    
    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)