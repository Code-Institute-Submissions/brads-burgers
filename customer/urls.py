from django.urls import path

from . import views

app_name = 'customer'

urlpatterns = [
    path('order', views.order, name='order'),
    path('burger', views.burger, name='burger'),
    path('side', views.side, name='side'),
    path('drink', views.drink, name='drink'),
]
