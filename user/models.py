from django.db import models


class UserProfile(models.Model):
    class Meta:
        db_table = "profile"

    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True)
    balance = models.IntegerField(default=10_000)
