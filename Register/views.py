from django.shortcuts import render
#importación de elementos de rest_framework
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
#importacion de serializer
from Register.serializers import RegisterUser

# Create your views here.
class UserApi(APIView):
    def post(self, request):
        serializer = RegisterUser(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
