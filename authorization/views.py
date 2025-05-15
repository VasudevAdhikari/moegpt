from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
import json
# Create your views here.

def get_username_by_email(email):
    try:
        user = User.objects.get(email=email)
        return user.username
    except User.DoesNotExist:
        return None
####################################################################################

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('mail')
        pwd = request.POST.get('pwd')
        print(email, pwd)
        # Get the username associated with the email
        username = get_username_by_email(email)
        print(username)
        print(pwd)
        # Authenticate the user
        user = authenticate(request, username=username, password=pwd)
        # print(user.email)
        if user is not None:
            login(request, user)  # Log the user in
            messages.success(request, 'Login successful!')
            return redirect('/chatbot/')  # Redirect to a home page or dashboard
        else:
            return render(request, 'login.html', {'message': f'Wrong password for {email}'})

    return render(request, 'login.html')
####################################################################################

def is_unique_username(username):
    return not User.objects.filter(username=username).exists()
####################################################################################

def is_unique_email(email):
    return not User.objects.filter(email=email).exists()
####################################################################################

def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        email = request.POST.get('mail')
        pwd = request.POST.get('pwd')

        # Check if username and email are unique
        if not (is_unique_username(username) and is_unique_email(email)):
            messages.error(request, "Username or email already exists.")
            return redirect('/register/')

        # Create a new user
        user = User(
            username=username,
            email=email
        )
        user.set_password(pwd)  # Hash the password
        user.save()  # Save the user to the database

        # Log the user in
        login(request, user)

        return redirect('/chatbot/')  # Redirect to the chatbot page

    return render(request, 'register.html')
####################################################################################

def user_logout(request):
    logout(request)  # Log the user out
    messages.success(request, 'You have been logged out successfully.')
    return redirect('/login/')
####################################################################################

def check_email(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('attribute')
        
        # Check if the email exists in the User table
        exists = User.objects.filter(email=email).exists()
        
        return JsonResponse({'exists': exists})
    
def check_username(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('attribute')
        print(username)
        # Check if the email exists in the User table
        exists = User.objects.filter(username=username).exists()
        
        return JsonResponse({'exists': exists})
####################################################################################
# Make sure you do NOT reference user.city anywhere in your code.