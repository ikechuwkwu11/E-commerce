from django.db import models
from users.models import User
# Create your models here.

class Vendors(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    store_name = models.CharField(max_length=30)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.store_name