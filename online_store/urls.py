from django.urls import path
from online_store.views import all_products, add_product, show_returns


urlpatterns = [
    path("all_products/", all_products, name="products"),
    path("add_product", add_product, name="add_product"),
    path("returns", show_returns, name="all_returns")
]