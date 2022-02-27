from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import RegexValidator
from users.managers import CustomUserManager
from django.utils import timezone

class User(AbstractBaseUser, PermissionsMixin):
    f_name = models.CharField(max_length=30,validators=[RegexValidator('([A-Z,a-z]+[\-\s]?)')], verbose_name="First Name")
    l_name = models.CharField(max_length=30, verbose_name="Last Name", validators=[RegexValidator('([A-Z,a-z]+[\-\s]?)')])
    email =  models.EmailField(max_length=254, unique=True, verbose_name="Email",)
    telephone = models.CharField(validators=[RegexValidator('^\+?1?\d{9,15}$')], max_length=17, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

