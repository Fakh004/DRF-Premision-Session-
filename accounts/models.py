from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    bio = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=13)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')