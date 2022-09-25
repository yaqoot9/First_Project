from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class post(models.Model):
    content=models.Text