from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'customer/index.html')

def order(request):
    return render(request, 'customer/order.html')
