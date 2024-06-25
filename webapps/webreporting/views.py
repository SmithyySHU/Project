from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def home(request) :
    return render (request, 'webreporting/home.html', {'title': 'Welcome to JobFinders'})

def about(request) :
    return render (request, 'webreporting/about.html', {'title': 'About JobFinders'})

def contact(request) :
    return render (request, 'webreporting/contact.html', {'title': 'Contact JobFinders'})

def register(request) :
    if request.method == 'POST' :
        form = UserCreationForm(request.POST)
        if form.is_valid() :
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect ('webreporting:home')
    else :
        form = UserCreationForm()
    return render (request, 'users/register.html', {'form': form, 'title': 'Register for JobFinders'})
