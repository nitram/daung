from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    return HttpResponseRedirect(reverse("management:index"))


def create_page(request):
    if request.method == "POST":
        first_name = request.POST["firstname"]
        last_name = request.POST["lastname"]
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]

        user = User.objects.create_user(username=username, 
                                        first_name=first_name, 
                                        last_name=last_name, 
                                        email=email, 
                                        password=password)
        
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("inventory:index"))
        else:
            return render(request, "users/create.html", {
                "form_data": {
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email,
                    'username': username,                    
                },
                "message": "Invalid user information. Try again"
            })

    return render(request, "users/create.html")


# Create your views here.
def login_page(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request,
                            username=username,
                            password=password)
            
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("inventory:index"))
        else:
            return render(request, "users/login.html", {
                "form_data": {
                    'username': username,
                },
                "message": "Invalid credentials"
            })

    return render(request, "users/login.html")


def logout_page(request):
    logout(request)
    return render(request, "users/login.html", {
        "message": "Logged out"
    })