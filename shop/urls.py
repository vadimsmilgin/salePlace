from shop.views import *
from django.urls import path, re_path

app_name = 'shop'

urlpatterns = [
    path('', ProductList.as_view(), name='index'),
    re_path(r'^(?P<slug>[-\w]+)$', SingleProduct.as_view(), name='detail'),
    re_path(r'^categories/(?P<slug>[-\w]+)$', SingleCategory.as_view(), name='shop_category'),
    re_path(r'^deleteItem/(?P<item_id>\d+)/$', deleteItem, name='deleteItem'),
]