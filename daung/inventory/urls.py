from django.urls import path

from . import views

app_name = "inventory"

urlpatterns = [
    path("", views.index, name="index"),
    path("items/", views.items, name="items"),
    path("add_bin/", views.add_bin, name="add_bin"),
    path("add_item/", views.add_item, name="add_item"),
]