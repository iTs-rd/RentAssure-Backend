from rest_framework import serializers
from .models import Flat, Room, House
# from .models import Image

# class ImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model= Image
#         fields= ('id','img1','img2')

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ('id' ,'title','img1','img2','img3','img4', 'bedroom', 'bathroom', 'balconies', 'area', 'furnished', 'price', 'additional_charge', 'security_money', 'locality', 'address', 'city', 'state', 'pin', 'phone', 'available', 'parking', 'agreement_duration', 'description')

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id','img1','img2','img3','img4' ,'title', 'bathroom', 'balconies', 'ac', 'water', 'electricity', 'area', 'furnished', 'price', 'additional_charge', 'security_money', 'locality', 'address', 'city', 'state', 'pin', 'phone', 'available', 'parking', 'agreement_duration', 'description')

class FlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flat
        fields = ('id','img1','img2','img3','img4' ,'title', 'bedroom', 'floor', 'bathroom', 'balconies', 'area', 'furnished', 'price', 'additional_charge', 'security_money', 'locality', 'address', 'city', 'state', 'pin', 'phone', 'available', 'parking', 'agreement_duration', 'description')
