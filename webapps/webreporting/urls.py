from django.contrib import admin
from django.urls import include, path
from users import views as user_views
from django.contrib.auth import views as auth_views
from .views import JobListView, JobDetailView, benefit_calculator
from . import views

app_name = 'webreporting'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),
    path('job/', JobListView.as_view(), name='job'),
    path('job/<int:pk>/', JobDetailView.as_view(), name='job-detail'),
    path('calculator/', benefit_calculator, name='benefit_calculator'),
]
