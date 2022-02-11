from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    class Meta:
        db_table = "profile"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True)
    balance = models.IntegerField(default=10_000)
