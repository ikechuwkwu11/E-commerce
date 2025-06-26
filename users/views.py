from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import RegisterSerializer,LoginSerializer
from .models import User
from rest_framework import status
from django.contrib.auth import logout

class Register(APIView):
    def post(self,request):
        try:
            serializer = RegisterSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'You have successfully registered.. Now login!'},status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class Login(APIView):
    def post(self,request):
        try:
            serializer = LoginSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'You have successfully logged in!'},status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class Logout(APIView):
    def get(self, request):
        try:
            logout(request)
            return Response({'message':'You have been logged out!'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':'Internal server error', 'error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetUser(APIView):
    def get(self,request):
        try:
            user = User.objects.all()
            serializer = RegisterSerializer(user,many=True)
            return Response({'message':'This are all the registered people','data':serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)