from django.shortcuts import render
from rest_framework.decorators import  api_view
from .serializers import UserSerializ
from rest_framework.response import Response
from django.contrib.auth import authenticate,login,logout
from rest_framework import status
from django.shortcuts import  get_object_or_404,redirect,HttpResponseRedirect,reverse
# Create your views here.
@api_view(['POST'])
def register (requset):
    serializer= UserSerializ(data=requset.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response (serializer.data)

@api_view(['POST'])
def log_in(request):
    context={}
    username = request.data['username']
    password = request.data['password']
    user = authenticate(request, username=username, password=password)
    if user:
        login(request, user)
        return HttpResponseRedirect(reverse('Register'))

    else:
        context["error"] = "provide valid credentials!"
        return Response(status=status.HTTP_401_UNAUTHORIZED)




