from rest_framework import serializers
from django.contrib.auth.models import User
from .models import User_profile,post
class UserSerializ(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']



class ProfileSerializ(serializers.ModelSerializer):
    class Meta:
        model=User_profile
        fields=['date_to_birth','gender','marital_status']

class PostSerializ(serializers.ModelSerializer):
    class Meta:
        model=post
        fields=['content']
