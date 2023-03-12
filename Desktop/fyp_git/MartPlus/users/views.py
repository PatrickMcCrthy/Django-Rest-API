from unittest import loader
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
# from .decorators import unauthenticated_user, allowed_users, auctioneer_only

def home(request):
    return render(request, 'users/home.html')

# @auctioneer_only
def auctioneer_dashboard(request):
  template = loader.get_template('auctioneer_dashboard.html')
  return HttpResponse(template.render())

# @unauthenticated_user
def login(request):
    if request.method == "POST":
        pass
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        messages.success(request, ("ERROR"))
        return redirect('login')

# @unauthenticated_user
def register(request):
    if request.method == 'POST':
     name = request.POST.get('username')
     firstname = request.POST.get('firstname')
     lastname = request.POST.get("lastname")
     email = request.POST.get("email")
     password = request.POST.get("password")
     confirmpassword = request.POST.get("confirmpassword")

     my_user=User.objects.create_user(name, email, password)
     my_user.first_name = firstname
     my_user.last_name = lastname

     my_user.save()

    # return redirect('login')
    
    return render(request, 'users/register.html', {})


# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()

#             messages.success(request, f'Your account has been created. You can log in now!')
#             return redirect('login')
#     else:
#         form = UserRegistrationForm()

#     context = {'form': form}
    # return render(request, 'users/register.html', context)