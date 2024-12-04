from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def home(request):
    return render(request, 'member/home.html')

def events(request):
    return render(request, 'member/event.html')

def donate(request):
    return render(request, 'member/donate.html')

def gallery(request):
    return render(request, 'member/gallery.html')

