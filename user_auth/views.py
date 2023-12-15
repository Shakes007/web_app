
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
# Function to handle User logins.
def user_login(request):
    return render(request, 'authentication/login.html')


# Function to authenticate a user.
def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    # If user does not exist, return user back to login page,
    # if user does exist, return user to a new html file.
    if user is None:
        return HttpResponseRedirect(
            reverse('user_auth:login')
        )
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('notesync:tour_dates')
        )


# Function to display a register form for new users.
def user_registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(
                reverse('notesync:tour_dates')
                )
    else:
        form = UserCreationForm

    return render(request, 'authentication/registration.html', {'form': form})
