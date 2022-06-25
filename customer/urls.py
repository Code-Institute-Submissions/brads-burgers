from django.urls import path

from . import views

app_name = 'customer'

urlpatterns = [
    path('orer', views.order, name='order'),
]