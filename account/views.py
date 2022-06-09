from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def account(request):
    return render(request, 'account/base.html')

def getaccount(request, id):
    return render(request, 'account/home.html', {'id': id})
