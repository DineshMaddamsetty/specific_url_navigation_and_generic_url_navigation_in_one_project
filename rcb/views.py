from django.shortcuts import render

from django.http import HttpResponse


def virat(request):
    return render(request,'virat.html')

def VIRAT(request):
    return HttpResponse('VIRAT is Good Man ')

