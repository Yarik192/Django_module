from django.forms import ModelForm
from online_store.models import Product, Purchase


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class PurchaseForm(ModelForm):
    class Meta:
        model = Purchase
        fields = "__all__"
