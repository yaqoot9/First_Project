from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.decorators import  api_view
from .serializers import UserSerializ,ProfileSerializ,PostSerializ
from rest_framework.response import Response
from django.contrib.auth import authenticate,login,logout
from rest_framework import status
from django.shortcuts import  get_object_or_404,redirect,HttpResponseRedirect,reverse
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .models import User_profile,post
from rest_framework.permissions import IsAuthenticated
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
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

    else:
        context["error"] = "provide valid credentials!"
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class Add(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self,request):
        user=request.user
        ser = ProfileSerializ( data=request.data)
        if ser.is_valid(raise_exception=True):
            date_to_birth = request.data['date_to_birth']
            gender = request.data['gender']
            marital_status = request.data['marital_status']


            profile=User_profile.objects.create(
                user_id=user,
                date_to_birth=date_to_birth,
                gender=gender,
                marital_status=marital_status
            )


            profile.save()
        return Response(ser.data)



class Edit(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, pk):

        profile = User_profile.objects.get(id=pk)
        ser = ProfileSerializ(instance=profile, data=request.data)
        if ser.is_valid(raise_exception=True):
            ser.save()
        return Response(ser.data)




#CRUD

class CRUD(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self,request):
        user=request.user
        ser = PostSerializ( data=request.data)
        if ser.is_valid(raise_exception=True):
            content=request.data['content']
            p=post.objects.create(user_id=user,content=content)
            p.save()
        return Response(ser.data)

    def get(self, request):
        p = post.objects.all()
        serializer = PostSerializ(p, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        p = post.objects.get(id=pk)
        ser = PostSerializ(instance=p, data=request.data)
        if ser.is_valid(raise_exception=True):
            ser.save()
        return Response(ser.data)


    def delete(self,request,pk):
        p = post.objects.filter(id=pk).first()
        p.delete()
        return Response('Deleted!')


