from django.shortcuts import render
from django.http import HttpResponse
from .models import Charity

def home_page(request):
    return render(request, 'home_page.html')

def home(request):
    charity = Charity.objects.all()
    return render(request, 'home.html', {'charity': charity})

def reservation(request):
    return render(request, 'reservation.html')