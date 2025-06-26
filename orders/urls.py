from django.urls import path
from .views import AddOrder,GetOrder,SingleOrder,EditOrder,DeleteOrder

urlpatterns = [
    path('add_order/',AddOrder.as_view(),name='add_order'),
    path('get_order/',GetOrder.as_view(),name='get_order'),
    path('single_order/<int:order_id>',SingleOrder.as_view(),name='single_order'),
    path('edit_order/<int:order_id>',EditOrder.as_view(),name='edit_order'),
    path('delete_order/<int:order_id>',DeleteOrder.as_view(),name='delete_order')
]