from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Bin(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.name}"
    

class Item(models.Model):
    name = models.CharField(max_length=128)
    quantity = models.PositiveIntegerField()
    image = models.ImageField(upload_to='items/', blank=True, null=True)
    bin = models.ForeignKey(Bin, on_delete=models.SET_NULL, related_name='items', blank=True, null=True)

    def __str__(self):
        return f"{self.name} | {self.quantity}"
    

class Log(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    username = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, blank=True, null=True)
    ondelete_last_item = models.CharField(max_length=255, blank=True, null=True)
    bin = models.ForeignKey(Bin, on_delete=models.SET_NULL, blank=True, null=True)
    ondelete_last_bin = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    previous_quantity = models.PositiveIntegerField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.timestamp} - {self.username} - {self.item.name}"
