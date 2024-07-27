from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse

from itertools import zip_longest

from .models import Bin, Item, Log

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    
    bins = Bin.objects.all()
    return render(request, "inventory/index.html", {'bins': bins})


# Create your views here.
def items(request, bin_id=None):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    
    if bin_id:
        bin_instance = get_object_or_404(Bin, id=bin_id)
        bins = Bin.objects.all()
        items = Item.objects.filter(bin=bin_instance)
        
        context = {
            'items': items,
            'selected_bin': bin_instance,
            'bins': bins,
        }
    else:
        bins = Bin.objects.all()
        items = Item.objects.all()
        
        context = {
            'items': items,
            'bins': bins,
        }

    return render(request, "inventory/items.html", context)


# Create your views here.
def add_bin(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    
    if request.method == "POST":
        name = request.POST.get('name')

        if name:
            Bin.objects.create(name=name)
            return redirect('inventory:edit_bin')
        
    return render(request, "inventory/add_bin.html")


# Create your views here.
def add_item(request, bin_id=None):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    
    bins = Bin.objects.all()

    if request.method == "POST":
        name = request.POST.get('name')
        quantity = request.POST.get('quantity')
        bin_id = request.POST.get('bin')

        image = request.FILES.get('image')

        if name and quantity:
            bin_instance = Bin.objects.get(id=bin_id) if bin_id else None
            Item.objects.create(
                name=name,
                quantity=quantity,
                image=image,
                bin=bin_instance,
            )
            return redirect('inventory:items')
    
    if bin_id:
        bin_instance = get_object_or_404(Bin, id=bin_id)
        context = {
            'bins': bins,
            'selected_bin': bin_instance
        }
    else:
        context = {'bins': bins}

    return render(request, "inventory/add_item.html", context)


def edit_bin(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    
    if request.method == "POST":
        bin_ids = request.POST.getlist('bin_ids')
        bin_names = request.POST.getlist('bin_names')
        original_bin_names = request.POST.getlist('original_bin_names')
        removed_bins = request.POST.getlist('removed_bins')
        
        errors = []
        
        # Iterate through each bin and update it
        for bin_id, bin_name, original_bin_name, removed_bin in zip_longest(
            bin_ids, bin_names, original_bin_names, removed_bins, fillvalue=None):
            try: 
                bin = Bin.objects.get(id=bin_id)
                if removed_bin == '1':
                    bin.delete()
                else:
                    bin.name = bin_name
                    bin.save()
            except Bin.DoesNotExist:
                # Handle the case where the bin has been deleted
                errors.append(f"You cannot change {original_bin_name} because it has been deleted by another user.")

        # Notify the user of the errors if there are any
        if errors:
            for error in errors:
                messages.error(request, error)

        # Redirect back to the index page
        return redirect('inventory:index')
    
    bins = Bin.objects.all()
    return render(request, "inventory/edit_bin.html", {'bins': bins})


def edit_item(request, bin_id=None):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    
    if request.method == "POST":
        item_ids = request.POST.getlist('item_ids')
        item_names = request.POST.getlist('item_names')
        original_item_names = request.POST.getlist('original_item_names')
        item_qtys = request.POST.getlist('item_qtys')
        original_item_qtys = request.POST.getlist('original_item_qtys')
        item_imgs = request.FILES.getlist('item_imgs')
        removed_items = request.POST.getlist('removed_items')

        errors = []
        
        # Iterate through each item and update it
        for item_id, item_name, original_item_name, item_qty, original_item_qty, item_img, removed_item in zip_longest(
            item_ids, item_names, original_item_names, item_qtys, original_item_qtys, item_imgs, removed_items, fillvalue=None):
            try: 
                item = Item.objects.get(id=item_id)

                if removed_item == '1':
                    item.delete()
                else:
                    if item.bin:
                        bin = item.bin 
                        bin_name = item.bin.name
                    else:
                        bin = None
                        bin_name = None

                    if item_qty != original_item_qty:
                        Log.objects.create(
                            username=request.user,
                            item=item,
                            ondelete_last_item = item.name,
                            bin = bin,
                            ondelete_last_bin = bin_name,
                            quantity = item_qty,
                            previous_quantity = original_item_qty
                        )

                    item.image = item_img
                    item.name = item_name
                    item.quantity = item_qty
                    item.save()
            except Item.DoesNotExist:
                # Handle the case where the item has been deleted
                errors.append(f"You cannot change {original_item_name} because it has been deleted by another user.")

        # Notify the user of the errors if there are any
        if errors:
            for error in errors:
                messages.error(request, error)

        # Redirect back to the index page
        return redirect('inventory:items')
    
    if bin_id:
        bin_instance = get_object_or_404(Bin, id=bin_id)
        bins = Bin.objects.all()
        items = Item.objects.filter(bin=bin_instance)
        
        context = {
            'items': items,
            'selected_bin': bin_instance,
            'bins': bins,
        }
    else:
        bins = Bin.objects.all()
        items = Item.objects.all()
        
        context = {
            'items': items,
            'bins': bins,
        }
    
    return render(request, "inventory/edit_item.html", context)


def item_logs(request, page=0):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    
    logs = Log.objects.order_by('-id')[20*page:20*(page+1)]
    bins = Bin.objects.all()

    context = {
        'logs': logs,
        'bins': bins,
        'next_page': page+1,
    }
    
    return render(request, "inventory/item_log.html", context)
