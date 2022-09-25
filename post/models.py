from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class post(models.Model):
    content=models.TextField()
    Created=models.DateTimeField(auto_now_add=True)
    Update=models.DateTimeField(auto_now_add=True)
    user_id=models.ForeignKey(User,models.CASCADE, related_name='post')


class User_profile(models.Model):
    Created = models.DateTimeField(auto_now_add=True)
    Update = models.DateTimeField(auto_now_add=True)
    date_to_birth=models.DateField()
    gender_choices=[("Famle",'F'), ("Male",'m')]
    gender=models.CharField(max_length=10,choices=gender_choices)
    marital_status=models.CharField(max_length=20)
    user_id = models.ForeignKey(User, models.CASCADE, related_name='User_Profile')



