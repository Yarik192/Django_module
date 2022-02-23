from django.urls import path
from online_store.views import ProductsListView, AddProductFormView, EditProductUpdateView, \
     show_returns, MyPurchaseListView


urlpatterns = [
    path("all_products/", ProductsListView.as_view(), name="products"),
    path("add_product/", AddProductFormView.as_view(), name="add_product"),
    path("returns/", show_returns, name="all_returns"),
    path("product/<int:pk>/", EditProductUpdateView.as_view(), name="edit_product"),
    path("my_purchase/", MyPurchaseListView.as_view(), name="my_purchase")
]