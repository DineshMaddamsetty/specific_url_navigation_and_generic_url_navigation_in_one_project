from django.shortcuts import render
from django.http import HttpResponse


def dhoni(request):
    return render(request,'dhoni.html')

def DHONI(request):
    return HttpResponse('Dhoni is Bad Man ')


# Create your views here.
