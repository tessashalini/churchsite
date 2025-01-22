from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.contrib.auth.models import User 
from django.contrib import messages
from django.conf import settings
from member.models import EventRequest
from .forms import DocumentForm
from .models import Budget, Donation, Expense, Document
def home(request):
    return render(request, 'admin_layer/home.html')
# Admin Documents View
# def documents(request):
#     return render(request, 'admin_layer/documents.html')

# Admin Finance View
# def finance(request):
#     return render(request, 'admin_layer/finance.html')

# def events(request):
#     return render(request, 'admin_layer/events.html')

# @login_required


import logging
logger = logging.getLogger(__name__)

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import EventRequest
from django.utils import timezone
from datetime import timedelta
# In admin_layer/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import EventRequest

def events(request):
    # Fetch pending requests
    pending_requests = EventRequest.objects.filter(status="Pending")

    # Fetch approved events
    approved_events = EventRequest.objects.filter(status="Approve")

    # Handle POST request for approval, rejection, or deletion
    if request.method == "POST":
        event_id = request.POST.get("event_id")
        action = request.POST.get("action")
        event = EventRequest.objects.get(id=event_id)

        if action == "Approve":
            event.status = "Approve"
            event.save()
            messages.success(request, "Event has been approved successfully.")
        elif action == "Reject":
            event.status = "Rejected"
            event.save()
            messages.success(request, "Event has been rejected successfully.")
        elif action == "Delete":
            event.delete()
            messages.success(request, "Event has been deleted successfully.")

        return redirect('events')

    return render(
        request,
        "admin_layer/events.html",
        {
            "pending_requests": pending_requests,
            "approved_events": approved_events,
        }
    )


def approved_events_api(request):
    approved_events = EventRequest.objects.filter(status="Approved").values("title", "date", "description")  # Corrected status
    return JsonResponse(list(approved_events), safe=False)

from django.shortcuts import render
from django.contrib.auth.models import User  # Assuming using Django's User model

def member_list(request):
    members = User.objects.all()  # Fetch all users
    return render(request, 'admin_layer/members.html', {'members': members})



# @login_required
def documents(request):
    # if not request.user.groups.filter(name="Admin").exists():
    #     return redirect("no_access")

    documents = Document.objects.all()

    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("documents")
    else:
        form = DocumentForm()
    return render(request, "admin_layer/documents.html", {"form": form, "documents": documents})

# @login_required
def finance(request):
    # if not request.user.groups.filter(name="Admin").exists():
    #     return redirect("no_access")

    budgets = Budget.objects.all()
    donations = Donation.objects.all()
    expenses = Expense.objects.all()

    return render(request, "admin_layer/finance.html", {
        "budgets": budgets,
        "donations": donations,
        "expenses": expenses
    })

from django.http import JsonResponse

def approved_events_api(request):
    approved_events = EventRequest.objects.filter(status="Approve").values("title", "date", "description")
    return JsonResponse(list(approved_events), safe=False)

from django.http import JsonResponse
from .models import EventRequest

def booked_events_api(request):
    # Fetch events with the status 'Approved' or 'Booked'
    events = EventRequest.objects.filter(status='Approve').values('title', 'date')
    event_list = [
        {
            'title': event['title'],
            'start': event['date'].isoformat(),  # Ensure date is in ISO format
        }
        for event in events
    ]
    return JsonResponse(event_list, safe=False)

from django.contrib.auth import logout
from django.shortcuts import redirect

def simple_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('public:home')  # Ensure 'home' is the correct URL name for public/home.html
    return redirect('public:home')

# views.py
# member/views.py
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.admin_profile.role == 'admin':  # Use the correct related_name
            login(request, user)
            return redirect('/adminlayer')  # Redirect to admin home
        else:
            messages.error(request, 'Invalid credentials or not an admin.')
    return render(request, 'member/admin_login.html')


from django.utils import timezone
from django.db.models import Sum
from django.shortcuts import render
from member.models import Donation
from .models import Expense

def home(request):
    donations_this_month = Donation.objects.aggregate(total=Sum('amount'))['total'] or 0.00
    # Calculate total events for the current month
    current_month = timezone.now().month
    current_year = timezone.now().year
    total_events = EventRequest.objects.filter(date__month=current_month).count()
    pending_events_count = EventRequest.objects.filter(status="Pending").count()
    expenses_this_month = Expense.objects.filter(date__year=current_year, date__month=current_month).aggregate(Sum('amount'))['amount__sum'] or 0
    
    dummy_expenses = [
        {'category': 'Rent', 'amount': 500, 'date': '2023-10-01'},
        {'category': 'Utilities', 'amount': 200, 'date': '2023-10-02'},
        {'category': 'Salaries', 'amount': 1500, 'date': '2023-10-03'},
        {'category': 'Office Supplies', 'amount': 300, 'date': '2023-10-04'},
        {'category': 'Travel', 'amount': 400, 'date': '2023-10-05'},
        {'category': 'Marketing', 'amount': 600, 'date': '2023-10-06'},
        {'category': 'Insurance', 'amount': 250, 'date': '2023-10-07'},
        {'category': 'Maintenance', 'amount': 350, 'date': '2023-10-08'},
        {'category': 'Miscellaneous', 'amount': 150, 'date': '2023-10-09'},
        {'category': 'Training', 'amount': 100, 'date': '2023-10-10'},
    ]
    return render(
        request,
        "admin_layer/home.html",
        {
            'total_events': total_events,
            'pending_events_count': pending_events_count,
            'donations_this_month': donations_this_month,
            "dummy_expenses": dummy_expenses,
            # 'expenses_this_month': expenses_this_month,
            # Add other context variables as needed
        }
    )

