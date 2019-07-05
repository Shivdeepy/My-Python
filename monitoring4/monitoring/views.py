from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    #return HttpResponse ("<h1> Welcome To GreyOrange NOC 2.0 </h1>")
    return render(request, 'index.html')

def home(request):
    inp= request.POST.get('username')
    inp1="Hi "+inp+","

    return render(request, 'home.html',{'data':inp1})

# Create your views here.
