from online_store.models import Product, Purchase
from django import forms


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ["count"]
