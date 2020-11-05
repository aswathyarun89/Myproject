from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myfun(request):
    return HttpResponse("Hello World")
def fun(request):
    return HttpResponse("<h1>My first Page</h1>")
def myfunction(request):
    return render(request,'sample.html')