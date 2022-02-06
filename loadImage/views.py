from asyncio import exceptions
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import os.path

#Importaciones de modelos
from loadImage.models import ImageTable

#Importacion de serializers
from loadImage.serializers import ImageTableSerializers

class LoadImageTable(APIView):
    def response_custom(self, messages, pay_load, status):
        responseOk={"messages":messages, "pay_load":pay_load, "status": status}
        return responseOk
    
    def get(self, request, format=None):
        queryset = ImageTable.objects.all()
        serializer = ImageTableSerializers(queryset, many = True, context = {'request':request})
        responseOk = self.response_custom("Succes", serializer.data, status=status.HTTP_200_OK)
        return Response(responseOk)
    
    def post(self, request):
        if 'image' not in request.data:
            raise exceptions.ParseError("No se ha seleccionado un archivo")
        archivos = request.data['image']
        name, formato = os.path.splitext(archivos.name)
        urlT=os.path.splitext(archivos.name)
        url=''.join(urlT)
        url='http://localhost:8000/media/img/'+url
        request.data['name_img'] = name
        request.data['format_img'] = formato
        request.data['url_img'] = url
        serializer = ImageTableSerializers(data=request.data)   
        if serializer.is_valid():
            validated_data = serializer.validated_data
            imagen = ImageTable(**validated_data)
            imagen.save()
            serializer_response = ImageTableSerializers(imagen)
            return Response(self.response_custom("Succes", serializer_response.data, status=status.HTTP_201_CREATED))
        return Response(self.response_custom("Error", serializer.errors, status=status.HTTP_400_BAD_REQUEST))


class LoadImageTableDetail(APIView):
    def response_custom(self, messages, pay_load, status):
        responseOk={"messages":messages, "pay_load":pay_load, "status": status}
        return responseOk
    
    def get_object(self, pk):
        try:
            return ImageTable.objects.get(pk = pk)
        except ImageTable.DoesNotExist:
            return 0

    def get(self, request,pk, format=None):
        idResponse = self.get_object(pk)
        if idResponse != 0:
            idResponse = ImageTableSerializers(idResponse)
            return Response(self.response_custom("Succes", idResponse.data , status=status.HTTP_200_OK))
        return Response(self.response_custom("Error", "No hay datos", status = status.HTTP_400_BAD_REQUEST))
    
    
    def put(self, request,pk, format=None):
        idResponse = self.get_object(pk)
        if 'image' not in request.data:
            raise exceptions.ParseError("No se ha seleccionado un archivo")
        archivos = request.data['image']
        name, formato = os.path.splitext(archivos.name)
        urlT=os.path.splitext(archivos.name)
        url=''.join(urlT)
        url='http://localhost:8000/media/img/'+url
        request.data['name_img'] = name
        request.data['format_img'] = formato
        request.data['url_img'] = url
        serializer = ImageTableSerializers(idResponse, data=request.data)   
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(self.response_custom("Succes", datas, status=status.HTTP_201_CREATED))
        return Response(self.response_custom("Error", serializer.errors,status = status.HTTP_400_BAD_REQUEST))

    def delete(self, request, pk):
        idResponse = self.get_object(pk)
        if idResponse != 0:
            idResponse.image.delete()
            idResponse.delete()
            return Response(self.response_custom("Succes","Eliminado", status=status.HTTP_204_NO_CONTENT))
        return Response(self.response_custom("Error", "Dato no encontrado",status = status.HTTP_400_BAD_REQUEST))