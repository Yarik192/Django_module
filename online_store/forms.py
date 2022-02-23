from online_store.models import Product, Purchase, ReturnPurchase
from django import forms


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ["count"]


class ReturnPurchaseForm(forms.ModelForm):
    class Meta:
        model = ReturnPurchase
        fields = []
