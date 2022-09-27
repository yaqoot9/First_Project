from django.contrib import admin

# Register your models here.
from .models import User_profile,post
admin.site.register(post)
admin.site.register(User_profile)