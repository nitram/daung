from django.db import models

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
    
