from django.shortcuts import render
from django.http import HttpResponse
import requests
def clrmry(request):
	
    #return HttpResponse ("<h1> Memory Clearance Page </h1>")
    
    return render(request, 'clrmry.html')


# Create your views here.
