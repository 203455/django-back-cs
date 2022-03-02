from django.shortcuts import render
#importación de elementos de rest_framework
from rest_framework.views import APIView
#importacion de serializer
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny

# Create your views here.
class UserApi(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    """ def post(self, request):
        serializer = RegisterUser(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) """
        
        
