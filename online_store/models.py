from django.db import models


class Product(models.Model):
    name_of_product = models.CharField(max_length=60)
    about_of_product = models.TextField(help_text="Расскажите о товаре")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.IntegerField()

    def __str__(self):
        return self.name_of_product

    class Meta:
        ordering = ["name_of_product"]
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Purchase(models.Model):
    customer = ...
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField()

    def __str__(self):
        return self.customer, self.product
