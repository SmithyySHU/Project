from django.shortcuts import render, redirect



# Create your views here.
def home(request) :
    return render (request, 'webreporting/home.html', {'title': 'Welcome to JobFinders'})

def about(request) :
    return render (request, 'webreporting/about.html', {'title': 'About JobFinders'})

def contact(request) :
    return render (request, 'webreporting/contact.html', {'title': 'Contact JobFinders'})

