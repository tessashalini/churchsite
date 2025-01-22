from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import EventRequestForm
from .models import EventRequest
from .forms import DonationForm
from .models import Donation

# Create your views here.

def home(request):
    return render(request, 'member/home.html')

# def events(request):
#     return render(request, 'member/event.html')

# def donate(request):
#     return render(request, 'member/donate.html')

def gallery(request):
    return render(request, 'member/gallery.html')

def thank_you(request):
    return render(request, 'member/thank_you.html')


# @login_required

def donate(request):
    return render(request, 'member/donate.html')



from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import EventRequestForm

from django.http import JsonResponse

def events(request):
    if request.method == "POST":
        form = EventRequestForm(request.POST)
        if form.is_valid():
            event_request = form.save(commit=False)
            event_request.status = "Pending"
            event_request.save()
            return JsonResponse({'success': True, 'message': "Your request is successfully submitted."})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = EventRequestForm()

    return render(request, "member/event.html", {"form": form})



from django.contrib.auth import logout
from django.shortcuts import redirect

def simple_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('public:home')  # Ensure 'home' is the correct URL name for public/home.html
    return redirect('public:home')



from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def switch_roles(request):
    # Redirect to the admin login page
    return redirect('/admin/')

from django.http import JsonResponse
from .models import EventRequest

# In member/views.py
from django.http import JsonResponse
from .models import EventRequest

def booked_events_api(request):
    events = EventRequest.objects.filter(status='Approve').values('title', 'date')
    event_list = [
        {
            'title': event['title'],
            'start': event['date'].isoformat(),  # Use only the date field
        }
        for event in events
    ]
    return JsonResponse(event_list, safe=False)


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

# member/views.py

# member/views.py

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

from accounts.models import Profile

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            try:
                # Use the correct related_name to access the Profile
                if user.accounts_profile.role == 'admin':
                    login(request, user)
                    return redirect('/adminlayer')  # Redirect to admin home
            except Profile.DoesNotExist:
                messages.error(request, 'Profile does not exist for this user.')
        else:
            messages.error(request, 'Invalid credentials or not an admin.')
    return render(request, 'member/admin_login.html')





# member/views.py
from django.shortcuts import render
from .forms import DonationForm

def donate(request):
    if request.method == 'POST':
        form = DonationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Donation successfully made!")
            # Add a success message or redirect if needed
    else:
        form = DonationForm()
    return render(request, 'member/donate.html', {'form': form})

# member/views.py

# member/views.py

from django.shortcuts import render
from django.http import JsonResponse
from .forms import CommunityMessageForm
from .models import CommunityMessage  # Ensure this line is present

def community(request):
    if request.method == 'POST':
        print("Received POST request with data:", request.POST)  # Debugging line
        form = CommunityMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': "Message submitted!"})
        else:
            print("Form errors:", form.errors)  # Debugging line
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = CommunityMessageForm()

    messages = CommunityMessage.objects.all().order_by('-submitted_at')
    return render(request, 'member/gallery.html', {'form': form, 'messages': messages})


