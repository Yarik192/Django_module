from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    class Meta:
        db_table = "profile"

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    balance = models.IntegerField(default=10_000, verbose_name="Кошелёк")

    def __str__(self):
        return str(self.user)
