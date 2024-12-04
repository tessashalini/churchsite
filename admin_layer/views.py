from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.contrib.auth.models import User 
from django.contrib import messages
from django.conf import settings
from events.forms import EventRequestForm  # Import the form
from events.models import EventRequest 

def home(request):
    return render(request, 'admin_layer/home.html')
# Admin Documents View
def documents(request):
    return render(request, 'admin_layer/documents.html')

# Admin Finance View
def finance(request):
    return render(request, 'admin_layer/finance.html')


def events(request):
    # Fetch pending and approved events (update based on your models)
    event_requests = EventRequest.objects.filter(is_approved=False)
    approved_events = EventRequest.objects.filter(is_approved=True)

    # Pass data to the template
    return render(request, 'admin_layer/events.html', {
        'event_requests': event_requests,
        'approved_events': approved_events,
    })
