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
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bin = models.ForeignKey(Bin, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return f"{self.name} | {self.quantity}"
    
