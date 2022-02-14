from django.db import models
from django.contrib.auth.models import User, AbstractUser


class CustomUser(AbstractUser):
    balance = models.PositiveIntegerField(default=10_000)
