from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request): 
    return HttpResponse("my Gallery for sites")

def country(request):
    return HttpResponse("country photo")

def about(request): 
    return render(request, 'gallery/about.html') #two arrgament in the templates files 