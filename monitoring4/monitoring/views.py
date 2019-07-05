from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    #return HttpResponse ("<h1> Welcome To GreyOrange NOC 2.0 </h1>")
    return render(request, 'home.html')

# Create your views here.
