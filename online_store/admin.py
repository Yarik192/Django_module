from django.contrib import admin
from online_store.models import Product, Purchase, ReturnPurchase


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name_of_product", "price", "quantity_in_stock"]


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ["customer", "product", "count"]


@admin.register(ReturnPurchase)
class ReturnPurchaseAdmin(admin.ModelAdmin):
    list_display = ["product", "time_of_request"]
