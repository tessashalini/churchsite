from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.contrib.auth.models import User 
from django.contrib import messages
from django.conf import settings


def home(request):
    return render(request, 'admin_layer/home.html')
# Admin Documents View
def documents(request):
    return render(request, 'admin_layer/documents.html')

# Admin Finance View
def finance(request):
    return render(request, 'admin_layer/finance.html')

def events(request):
    return render(request, 'admin_layer/events.html')
