from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import EventRequest
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from events.forms import EventRequestForm  # Import the form
from events.models import EventRequest  # Import the model
# Create your views here.

def home(request):
    return render(request, 'member/home.html')

def events(request):
    return render(request, 'member/event.html')

def donate(request):
    return render(request, 'member/donate.html')

def gallery(request):
    return render(request, 'member/gallery.html')

def get_events(request):
    events = EventRequest.objects.all().values('title', 'start', 'end')  # Customize fields as needed
    events_list = list(events)
    return JsonResponse(events_list, safe=False)

def request_event(request):
    if request.method == 'POST':
        form = EventRequestForm(request.POST)
        if form.is_valid():
            event_request = form.save(commit=False)
            event_request.member = request.user
            event_request.save()

            # Send email to the member
            send_mail(
                'Event Request Submitted',
                f"Your event request for '{event_request.title}' has been submitted for approval.",
                settings.DEFAULT_FROM_EMAIL,
                [event_request.email],
            )

            messages.success(request, "Your event request has been sent for approval.")
            return redirect('member:events')
    else:
        form = EventRequestForm()

    return render(request, 'member/request_event.html', {'form': form})
