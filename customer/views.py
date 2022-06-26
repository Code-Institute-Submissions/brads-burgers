from django.shortcuts import render
from django.http import HttpResponse
from .models import Burger, Side, Drink

def index(request):
    return render(request, 'customer/index.html')

def order(request):
    return render(request, 'customer/order.html')

def burger(request):
    burgers = Burger.objects.all()
    ctx = {'burgers': burgers}
    return render(request, 'customer/burger.html', ctx)

def side(request):
    sides = Side.objects.all()
    ctx = {'sides': sides}
    return render(request, 'customer/side.html', ctx)

def drink(request):
    drinks = Drink.objects.all()
    ctx = {'drinks': drinks}
    return render(request, 'customer/drink.html', ctx)
