from django.shortcuts import render


# Create your views here.
def home(request) :
    return render (request, 'webreporting/home.html')

def about(request) :
    return render (request, 'webreporting/about.html')

def contact(request) :
    return render (request, 'webreporting/contact.html')
