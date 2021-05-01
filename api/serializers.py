from rest_framework import serializers
from .models import Data


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'

class DataMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ('id','property_type' ,'img1','img2','img3','img4','title', 'area', 'furnished', 'rent','available_from','available_for','posted_on','posted_by')

