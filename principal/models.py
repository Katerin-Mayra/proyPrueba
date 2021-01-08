from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    ci = models.CharField(max_length=16, unique=True, null=False, blank=False)
    name = models.CharField(max_length=128, null=False, blank=False)
    last_name = models.CharField(max_length=128, null=False, blank=False)
    email = models.EmailField(max_length=150, null=False, blank=False, unique=True)
    phone = models.CharField(max_length=16, null=True, blank=False)
    whatsapp = models.CharField(max_length=16, null=True)
    image = models.CharField(max_length=150, null=True)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


#pass predet holamundo, 5520150-1O


