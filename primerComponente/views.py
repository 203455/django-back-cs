
from urllib import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#importacion de modelos agregados
from primerComponente.models import PrimerTabla
#importación de serializadores
from primerComponente.serializers import PrimerTablaSerializer
#importacion de tipo Json
import json


# Create your views here.



class PrimerTablaList(APIView):
    def response_custom(self, messages, pay_load, status):
        response_ok={"messages":messages, "pay_load":pay_load, "status": status}
        return response_ok
        
    
    def get(self, request, format=None):
        queryset=PrimerTabla.objects.all()
        serializer=PrimerTablaSerializer(queryset,many=True, context={'request':request})
        response_ok=self.response_custom("Succes", serializer.data, status=status.HTTP_200_OK)
        return Response(response_ok)
    
    def post(self, request, format=None):
        serializer=PrimerTablaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas=serializer.data
            return Response(self.response_custom("Succes", datas, status=status.HTTP_201_CREATED))
        return Response(self.response_custom("Error", serializer.errors, status=status.HTTP_400_BAD_REQUEST))

class PrimerTablaDetails(APIView):
    def response_custom(self, messages, pay_load, status):
        responseOk={"messages":messages, "pay_load":pay_load, "status": status}
        return responseOk
    
    def get_object(self, pk):
        try:
            return PrimerTabla.objects.get(pk=pk)
        except PrimerTabla.DoesNotExist:
            return 0
        
    def get(self, request, pk , format=None):
        id_response = self.get_object(pk)
        if id_response != 0:
            id_response = PrimerTablaSerializer(id_response)
            return Response(id_response.data, status=status.HTTP_200_OK)
        return Response('No hay datos', status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk , format=None):
        id_response = self.get_object(pk)
        serializer=PrimerTablaSerializer(id_response,data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(self.response_custom("Succes", datas, status=status.HTTP_201_CREATED))
        return Response(self.response_custom("Error", serializer.errors, status=status.HTTP_400_BAD_REQUEST))
    
    
    def delete(self, request, pk , format=None):
        id_response = self.get_object(pk)
        if id_response != 0:
            id_response.delete()
            return Response(self.response_custom("Succes", "Dato Eliminado", status=status.HTTP_201_CREATED))
        return Response(self.response_custom("Error", "Dato No Encontrado", status=status.HTTP_400_BAD_REQUEST))