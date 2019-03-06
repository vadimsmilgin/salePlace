from django.urls import path, re_path
from basket import views

app_name = 'basket'

urlpatterns = [
    re_path(r'^remove/(?P<item_id>\d+)/$', views.BasketRemove, name='BasketRemove'),
    re_path(r'^add/(?P<item_id>\d+)/$', views.BasketAdd, name='BasketAdd'),
    path('', views.Basket.as_view(), name='BasketDetail'),
]