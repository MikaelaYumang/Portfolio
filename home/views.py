from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib import messages

# Create your views here.
def home(request):
    #return HttpResponse("This is my homepage (/)")
    context={'name': 'Harry', 'course': 'Django'}
    return render(request, 'home.html', context)

def about(request):
    #return HttpResponse("This is my about page (/about)")
    return render(request, 'about.html')

def contact(request):
    #return HttpResponse("This is my contact page (/contact)")
    return render(request, 'contact.html')



