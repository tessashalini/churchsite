from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'public/home.html')

def about_us(request):
    return render(request, 'public/about_us.html')

def contact_us(request):
    return render(request, 'public/contact_us.html')


