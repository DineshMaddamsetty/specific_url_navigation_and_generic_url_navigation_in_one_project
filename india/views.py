from django.shortcuts import render
from django.http import HttpResponse


def padikal(request):
    return render(request,'padikal.html')

def PADIKAL(request):
    return HttpResponse('PADIKAL is good bat man')

# Create your views here.
