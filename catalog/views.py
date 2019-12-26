from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def welcome(request):
    return HttpResponse("<h1 style='color:blue'>Welcome To Catalog Application!</h1>")


def greet(request):
    if 'name' in request.GET:
        name = request.GET['name']
    else:
        name = "Guest"

    hours = datetime.now().hour
    if hours < 12:
        msg = "Good Morning"
    elif hours < 17:
        msg = "Good Afternoon"
    else:
        msg = "Good Evening"

    return HttpResponse(f"<h1>{msg} {name}</h1>")


def wish(request):
    if 'name' in request.GET:
        name = request.GET['name']
    else:
        name = "Guest"

    hours = datetime.now().hour
    if hours < 12:
        msg = "Good Morning"
    elif hours < 17:
        msg = "Good Afternoon"
    else:
        msg = "Good Evening"

    return render(request, 'wish.html',
                  {'msg': msg, 'user': name})

def calculate_discount(request):
    if 'amount' in request.GET:   # request with data, so process it
        amount = float(request.GET['amount'])
        rate = float(request.GET['rate'])
        discount = amount * rate / 100
        return render(request, 'discount.html', {'discount' : discount})
    else:  # request without parameters(data)
        return render(request,'discount.html')