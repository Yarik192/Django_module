from django.urls import path
from online_store.views import ProductsListView, AddProductFormView, ShowReturnsListView, EditProductUpdateView, \
    ProductDetailView, show_returns

urlpatterns = [
    path("all_products/", ProductsListView.as_view(), name="products"),
    path("add_product/", AddProductFormView.as_view(), name="add_product"),
    path("returns/", show_returns, name="all_returns"),
    path("<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("product/<int:pk>/", EditProductUpdateView.as_view(), name="edit_product")
]