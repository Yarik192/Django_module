from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView

from online_store.models import Product, Purchase, ReturnPurchase
from online_store.forms import ProductForm


class ProductsListView(ListView):
    model = Product


class ShowReturnsListView(ListView):
    model = ReturnPurchase


def add_product(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            Product.objects.create(
                name_of_product=form.cleaned_data.get("name_of_product"),
                about_of_product=form.cleaned_data.get("about_of_product"),
                price=form.cleaned_data.get("price"),
                quantity_in_stock=form.cleaned_data.get("quantity_in_stock")
            )
            return HttpResponseRedirect("/")
    if request.method == "GET":
        form = ProductForm
    return render(request, "online_store/add_product.html", {"form": form})


def edit_product(request: HttpRequest) -> HttpResponse:
    context = {

    }
    return render(request, "online_store/edit_product.html", context)


def new_purchase(request: HttpRequest) -> HttpResponse:
    ...
