from django.urls import path
from online_store.views import ProductsListView, add_product, ShowReturnsListView


urlpatterns = [
    path("all_products/", ProductsListView.as_view(), name="products"),
    path("add_product/", add_product, name="add_product"),
    path("returns/", ShowReturnsListView.as_view(), name="all_returns")
]