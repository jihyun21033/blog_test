from django.shortcuts import render
from django.http import HttpResponse as HR

def index(request):
    return HR("Hello World!")
# Create your views here.
