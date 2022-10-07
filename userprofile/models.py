from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, unique=True, related_name="userprofile")
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    post_code = models.IntegerField()
    editor = models.BooleanField(default=False)

# Create your models here.
