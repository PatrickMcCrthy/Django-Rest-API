from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from users.views import auctioneer_dashboard
from users.views import home
from users.views import register

urlpatterns = [
    path('registration/', register, name='register'),
    path('', home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('auctioneer-dashboard/', auctioneer_dashboard, name='ds')
]