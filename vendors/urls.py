from django.urls import path
from .views import AddVendor,GetVendor,SingleVendor,EditVendor,DeleteVendor
urlpatterns = [
    path('add_vendor/',AddVendor.as_view(),name = 'add_vendor'),
    path('get_vendor/',GetVendor.as_view(),name='get_vendor'),
    path('single_vendor/<int:vendor_id>/',SingleVendor.as_view(),name='single_vendor'),
    path('edit_vendor/<int:vendor_id>',EditVendor.as_view(),name='edit_vendor'),
    path('delete_vendor/<int:vendor_id>',DeleteVendor.as_view(),name='delete_vendor')

]