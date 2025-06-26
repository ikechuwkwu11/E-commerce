from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    is_customer = models.BooleanField(default=True)
    is_seller = models.BooleanField(default=False)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
