from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, FormView, CreateView, UpdateView, DetailView

from online_store.models import Product, ReturnPurchase
from online_store.forms import ProductForm


class ProductsListView(ListView):
    model = Product


class ShowReturnsListView(ListView):
    model = ReturnPurchase


class ProductDetailView(DetailView):
    model = Product
    pk_url_kwarg = "pk"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class AddProductFormView(FormView):
    template_name = "online_store/add_product.html"
    form_class = ProductForm
    success_url = reverse_lazy("homepage")

    def form_valid(self, form):
        form.save()
        return super(AddProductFormView, self).form_valid(form)


class EditProductUpdateView(UpdateView):
    model = Product
    fields = "__all__"
    template_name = "online_store/edit_product.html"
    pk_url_kwarg = "pk"
    success_url = reverse_lazy("products")


def new_purchase(request: HttpRequest) -> HttpResponse:
    ...
