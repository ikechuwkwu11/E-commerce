from django.urls import path
from .views import AddProduct,GetProduct,SingleProduct,EditProduct,DeleteProduct

urlpatterns = [
    path('add_product/',AddProduct.as_view(),name='add_product'),
    path('get_product/',GetProduct.as_view(),name='get_product'),
    path('single_product/<int:product_id>',SingleProduct.as_view(),name='single_products'),
    path('edit_product/<int:product_id>',EditProduct.as_view(),name='edit_products'),
    path('delete_product/<int:product_id>',DeleteProduct.as_view(),name='delete_products')
]