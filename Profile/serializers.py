from rest_framework import serializers

#Importancion de modelos
from Profile.models import ProfileTable

class ProfileTableSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProfileTable
        fields = ('id_user','url_img','image')