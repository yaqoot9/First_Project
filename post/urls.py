from django.urls import path
from . import views

urlpatterns = [
    path('',views.log_in,name='Login'),
    path('register',views.register,name='Register'),
]
