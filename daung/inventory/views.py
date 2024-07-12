from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    
    # TODO: Get bins
    return render(request, "inventory/index.html", {})


# Create your views here.
def items(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    
    # TODO: Get items
    return render(request, "inventory/items.html", {})


# Create your views here.
def add_bin(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    
    return render(request, "inventory/add_bin.html")


# Create your views here.
def add_item(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    
    return render(request, "inventory/add_item.html")
         