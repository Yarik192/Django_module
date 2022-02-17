from datetime import timedelta
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, FormView, UpdateView, DetailView
from online_store.forms import PurchaseForm, ReturnPurchaseForm
from online_store.models import Product, ReturnPurchase, Purchase
from online_store.forms import ProductForm


class ProductsListView(ListView, FormView):
    model = Product
    form_class = PurchaseForm
    success_url = reverse_lazy("products")

    def form_valid(self, form):
        product = Product.objects.get(pk=self.request.POST["pk"])
        if int(self.request.POST.get("count")) > product.quantity_in_stock:
            messages.add_message(self.request, messages.ERROR, "В наличии такого количества нет")
            return redirect("products")
        elif self.request.user.balance < product.price * int(self.request.POST.get("count")):
            messages.error(request=self.request, message="Недостаточно средств")
            return redirect("products")
        else:
            self.request.user.balance -= product.price * int(self.request.POST.get("count"))
            self.request.user.save()
            product.quantity_in_stock -= int(self.request.POST.get("count"))
            product.save()
            Purchase.objects.create(
                customer=self.request.user,
                product=product,
                count=self.request.POST.get("count")
            )
            redirect("products")
            return super(ProductsListView, self).form_valid(form)


class AddProductFormView(FormView):
    template_name = "online_store/add_product.html"
    form_class = ProductForm
    success_url = reverse_lazy("products")

    def form_valid(self, form):
        Product.objects.create(name_of_product=self.request.POST["name_of_product"],
                               about_of_product=self.request.POST["about_of_product"],
                               price=self.request.POST["price"],
                               quantity_in_stock=self.request.POST["quantity_in_stock"])
        return super(AddProductFormView, self).form_valid(form)


def show_returns(request: HttpRequest) -> HttpResponse:
    object_list = ReturnPurchase.objects.all()
    context = {
        "object_list": object_list
    }
    if request.GET.get("confirm"):
        ...
    else:
        ...
    return render(request, "online_store/returnpurchase_list.html", context)


class ShowReturnsListView(ListView):
    model = ReturnPurchase


class ProductDetailView(DetailView):
    model = Product
    pk_url_kwarg = "pk"


class EditProductUpdateView(UpdateView):
    model = Product
    fields = "__all__"
    template_name = "online_store/edit_product.html"
    pk_url_kwarg = "pk"
    success_url = reverse_lazy("products")


class MyPurchaseListView(ListView, FormView):
    model = Purchase
    form_class = ReturnPurchaseForm
    template_name = "online_store/my_purchase.html"
    success_url = reverse_lazy("my_purchase")

    def form_valid(self, form):
        purchase = Purchase.objects.get(pk=self.request.POST["pk"])
        if purchase.date_of_purchase + timedelta(minutes=180) < timezone.now():
            print("Вернуть нельзя")
            return redirect("products")
        else:
            print("Вернуть можно")
            return redirect("my_purchase")
