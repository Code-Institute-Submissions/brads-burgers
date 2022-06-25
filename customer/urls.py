from django.urls import path

from . import views

app_name = 'customer'

urlpatterns = [
    path('order', views.order, name='order'),
    path('drink', views.drink, name='drink'),
]