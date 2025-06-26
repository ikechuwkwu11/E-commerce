from django.db import models
from vendors.models import Vendors
# Create your models here.

class Products(models.Model):
    vendor = models.ForeignKey(Vendors, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name