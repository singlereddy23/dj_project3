from django.http import HttpRequest
from django.shortcuts import render

def index(request):
    return HttpResponse("<h1>welcome to homepage</h1>")

def base(request):
    return render(request,"sample.html")

def demo1(request):
    return render(request,"pro/demo1.html")