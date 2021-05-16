from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import UserModel,DataModel


# password not included
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserModel
        # fields = '__all__'
        # fields= ('id','email','username','firstname','password')
        exclude= ['password','user_permissions','groups','is_active','is_staff','start_date','is_superuser','last_login']
        extra_kwargs={'password':{'write_only':True,'required':True}}


# password included
class UserSerializerPassword(serializers.ModelSerializer):
    class Meta:
        model=UserModel
        # fields = '__all__'
        # fields= ('id','email','username','firstname','password')
        exclude= ['dp','user_permissions','groups','is_active','is_staff','start_date','is_superuser','last_login']
        extra_kwargs={'password':{'write_only':True,'required':True}}

    def create(self,validated_data):
        user=UserModel.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user



class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataModel
        fields = '__all__'

class DataMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataModel
        fields = ('id','user','property_type' ,'img1','img2','img3','img4','title', 'area', 'furnished', 'rent','available_from','available_for','posted_on','posted_by')

