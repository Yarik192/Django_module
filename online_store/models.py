from django.contrib.auth.models import User
from django.db import models
# from users.models import UserProfile
from Django_module import settings


class Product(models.Model):
    name_of_product = models.CharField(max_length=60)
    about_of_product = models.TextField(help_text="Расскажите о товаре")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.PositiveIntegerField(default=0, help_text="Количество на складе")

    def __str__(self):
        return self.name_of_product

    class Meta:
        ordering = ["name_of_product"]
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Purchase(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)
    date_of_purchase = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.product)

    class Meta:
        verbose_name = "Покупка"
        verbose_name_plural = "Покупки"


class ReturnPurchase(models.Model):
    product = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    time_of_request = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.product)

    class Meta:
        verbose_name = "Возврат покупки"
        verbose_name_plural = "Возврат покупок"
