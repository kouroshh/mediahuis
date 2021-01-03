from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def hello_world(*args, **kwargs):
    return HttpResponse("<h1>Hello World!</h1>")


def offers(request):
    return render(request, 'pages/offers.html')
