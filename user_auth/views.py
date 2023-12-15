
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
# Function to handle User logins.
def user_login(request):
    '''
    Render the login page
    
    Args:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: The rendered login page.
    '''
    return render(request, 'authentication/login.html')


# Function to authenticate a user.
def authenticate_user(request):
    '''
    Authenticate a user based on provided username and password.
    
    Args:
        request (HttpRequest): The HTTP request object.
    
    Returns:
        HttpResponse: Redirects to the login page if authentication fails,
                      otherwise, redirects to a page for authenticated users.
    '''
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
    '''
    Display a registration form for new users
    
    Args:
        request (HttpRequest): The HTTP request object.
    
    Returns:
        HttpReponse: Render the registration form or redirects to a page for
                     authenticated users.
    '''

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
