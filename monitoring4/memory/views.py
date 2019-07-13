from django.shortcuts import render
from django.http import HttpResponse
import requests
import sys
import subprocess
sys.path.append('C:\\Users\\shivdeep.k\\Google Drive\\Programming\\Python\\Github\\My-Python\\monitoring4\\monitoring')
from monitoring.views import home


def clrmry(request):
	
    #return HttpResponse ("<h1> Memory Clearance Page </h1>")
    
    return render(request, 'clrmry.html')

def clrry(request):
    server= request.POST.get('Server')
    subprocess.Popen("start","//mnt//c//Windows//System32//cmd.exe", buff =0,shell= True)
    return HttpResponse (clrry)

    print(server)
    #return render(request, 'clrmry.html')