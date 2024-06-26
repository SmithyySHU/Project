from django.urls import path
from users import views as user_views 
from django.contrib.auth import views as auth_views

from . import views 

app_name = 'webreporting'

urlpatterns = [
    path ('', views.home, name = 'home'),
    path ('about', views.about, name = 'about'),
    path ('contact', views.contact, name = 'contact'),
    path ('register', user_views.register, name = 'register'),
    path('login', auth_views.LoginView.as_view(template_name = 'users/login.html'), name = 'login'),
    path('logout', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name='logout'),
]
