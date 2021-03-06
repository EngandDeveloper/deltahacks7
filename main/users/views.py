from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from users.models import *

# Create your views here.
def index(request):
    return render(request, 'users/index.html')

def loginPage(request):
    context = {}
    return render(request, 'users/login.html', context)

def registerPage(request):
    form = RegisterUser()
    context = {'form':form}
    #renders html file and sends context info to html page
    return render(request, 'users/register.html', context)

def logoutUser(request):
    logout(request)
    print("logoutUser view - user logout")
    return render(request, "users/index.html")

def loginUser(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            print("loginPage view - " + username + " logged in")
            #redirect user to profile page or somewhere
            # return render(request, 'users/userProfileRegister.html',context)
        else:
            messages.info(request, "Username OR password is incorrect")
            # return render(request, 'farms/login.html', context)
            return render(request, 'users/login.html', context)
    return render(request, 'users/login.html', context)

def registerUser(request):
    context = {}
    form = RegisterUser()
    #check whether the form method is POST if not don't allow saving for security reasons
    if request.method == 'POST':
        form = RegisterUser(request.POST)
        #(backend) check whether the form is valid or not
        if form.is_valid():
            form.save()
            print("register view.py - User is registered!")
            context = {'form':form}
            return render(request, 'users/login.html', context)
        else:
            messages.info(request, "An Error Occured! Account Has NOT Been Created.")
    #object to use backend data in html page
    context = {'form':form}
    return render(request, "users/register.html", context)