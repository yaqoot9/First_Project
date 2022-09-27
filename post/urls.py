from django.urls import path
from . import views

urlpatterns = [
    path('',views.log_in,name='Login'),
    path('register/',views.register,name='Register'),
    path('Add/',views.Add.as_view(),name='Add'),
    path('Edit<str:pk>/', views.Edit.as_view(), name='Edit'),
    path('CRUD/', views.CRUD.as_view(), name='CRUD'),
    path('CRUD<str:pk>/', views.CRUD.as_view(), name='CRUD'),

]
