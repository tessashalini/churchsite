from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'public/home.html')

def about_us(request):
    return render(request, 'public/about_us.html')




from django.shortcuts import render
from .forms import ContactForm
from .models import ContactSubmission

from django.core.mail import send_mail
from django.conf import settings

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            contact_submission = form.save()

            # Send a copy of the form to the user
            send_mail(
                'Your Contact Form Submission',
                f'Thank you for contacting us, {contact_submission.full_name}. Here is a copy of your submission:\n\n'
                f'Subject: {contact_submission.subject}\n'
                f'Question: {contact_submission.question}',
                settings.DEFAULT_FROM_EMAIL,
                [contact_submission.email],
                fail_silently=False,
            )

            return redirect('contact_us')  # Redirect to a thank you page after submission
    else:
        form = ContactForm()

    return render(request, 'public/contact_us.html', {'form': form})

from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


from django.contrib.auth import logout
from django.shortcuts import redirect

def simple_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')  # Redirect to home or any other page
    return redirect('/')  # Redirect to home or any other page

# public/views.py

from django.shortcuts import render

def custom_password_reset(request):
    if request.method == 'POST':
        # Handle form submission logic here
        pass
    else:
        # Render the password reset form
        return render(request, 'registration/password_reset_form.html')





