from asyncio import exceptions
from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import os.path

#Importaciones de modelos
from Profile.models import ProfileTable
from django.contrib.auth.models import User

#Importacion de serializers
from Profile.serializers import ProfileTableSerializers

class LoadProfileTable(APIView):
    def response_custom(self, messages, pay_load, status):
        response_ok={"messages":messages, "pay_load":pay_load, "status": status}
        return response_ok
    
    def get(self, request, format=None):
        queryset = ProfileTable.objects.all()
        serializer = ProfileTableSerializers(queryset, many = True, context = {'request':request})
        response_ok = self.response_custom("Succes", serializer.data, status=status.HTTP_200_OK)
        return Response(response_ok)
    
    def post(self, request):
        if 'image' not in request.data:
            raise exceptions.ParseError("No se ha seleccionado un archivo")
        archivos = request.data['image']
        url_text=os.path.splitext(archivos.name)
        url=''.join(url_text)
        url='http://localhost:8000/media/img/'+url
        request.data['url_img'] = url
        serializer = ProfileTableSerializers(data=request.data)   
        if serializer.is_valid():
            validated_data = serializer.validated_data
            imagen = ProfileTable(**validated_data)
            imagen.save()
            serializer_response = ProfileTableSerializers(imagen)
            return Response(self.response_custom("Succes", serializer_response.data, status=status.HTTP_201_CREATED))
        return Response(self.response_custom("Error", serializer.errors, status=status.HTTP_400_BAD_REQUEST))


class LoadProfileTableDetail(APIView):
    def response_custom(self, messages, pay_load, status):
        response_ok={"messages":messages, "pay_load":pay_load, "status": status}
        return response_ok
    
    def get_object(self, pk):
        try:
            return ProfileTable.objects.get(id_user = pk)
        except ProfileTable.DoesNotExist:
            return 0

    def get(self, request,pk, format=None):
        id_response = self.get_object(pk)
        if id_response != 0:
            id_response = ProfileTableSerializers(id_response)
            return Response(self.response_custom("Succes", id_response.data , status=status.HTTP_200_OK))
        return Response(self.response_custom("Error", "No hay datos", status = status.HTTP_400_BAD_REQUEST))
    
    
    def put(self, request,pk, format=None):
        id_response = self.get_object(pk)
        if 'image' not in request.data:
            raise exceptions.ParseError("No se ha seleccionado un archivo")
        id_response.image.delete()
        archivos = request.data['image']
        url_text=os.path.splitext(archivos.name)
        url=''.join(url_text)
        url='http://localhost:8000/media/img/'+url
        request.data['url_img'] = url
        serializer = ProfileTableSerializers(id_response, data=request.data)   
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(self.response_custom("Succes", datas, status=status.HTTP_201_CREATED))
        return Response(self.response_custom("Error", serializer.errors,status = status.HTTP_400_BAD_REQUEST))

    def delete(self, request, pk):
        id_response = self.get_object(pk)
        if id_response != 0:
            id_response.image.delete()
            id_response.delete()
            return Response(self.response_custom("Succes","Eliminado", status=status.HTTP_204_NO_CONTENT))
        return Response(self.response_custom("Error", "Dato no encontrado",status = status.HTTP_400_BAD_REQUEST))
    
class LoadUserDetails(APIView):
    
    def rest_costum(self,user,status):
        response = {
            "first_name": user[0]['first_name'],
            "last_name": user[0]['last_name'],
            "username": user[0]['username'],
            "email": user[0]['email'],
            "status": status
        }
        return response
    
    def get(self, request, pk, format=None):
        idresponse= User.objects.filter(id=pk).values()
        if(idresponse!=404):
            response_data= self.rest_costum(idresponse,status.HTTP_200_OK)
            return Response(response_data)
        return "No se encontró el usuario"
    
    def put(self, request, pk, format=None):
        data=request.data
        user = User.objects.filter(id=pk)
        user.update(username=data.get('username'))
        user.update(first_name=data.get('first_name'))
        user.update(last_name=data.get('last_name'))
        user.update(email=data.get('email'))
        response_user=User.objects.filter(id=pk).values()
        return Response(self.rest_costum(response_user,status.HTTP_200_OK))