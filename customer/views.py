from django.shortcuts import render
from django.http import HttpResponse
from .models import Drink

def index(request):
    return render(request, 'customer/index.html')

def order(request):
    return render(request, 'customer/order.html')

def drink(request):
    drinks = Drink.objects.all()
    ctx = {'drinks': drinks}
    return render(request, 'customer/drink.html', ctx)
