from django.urls import path

from . import views

app_name = "inventory"

urlpatterns = [
    path("", views.index, name="index"),
    path("items/", views.items, name="items"),
    path("items/b/<int:bin_id>", views.items, name="bin_items"),
    path("add_bin/", views.add_bin, name="add_bin"),
    path("add_item/", views.add_item, name="add_item"),
    path("add_item/<int:bin_id>", views.add_item, name="add_bin_item"),
    path("edit_bin/", views.edit_bin, name="edit_bin"),
]