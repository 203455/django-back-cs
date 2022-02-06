from rest_framework import serializers

#Importancion de modelos
from loadImage.models import ImageTable

class ImageTableSerializers(serializers.ModelSerializer):
    class Meta:
        model = ImageTable
        fields = ('pk','name_img','format_img', 'url_img', 'image')
        