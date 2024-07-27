from django.contrib import admin
from .models import Bin, Item, Log

admin.site.register(Bin)
admin.site.register(Item)
admin.site.register(Log)