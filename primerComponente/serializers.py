from dataclasses import fields
from pyexpat import model
from rest_framework import routers, serializers, viewsets

#importación de modelos
from primerComponente.models import PrimerTabla

class PrimerTablaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimerTabla
        fields = ('nombre', 'edad')
        