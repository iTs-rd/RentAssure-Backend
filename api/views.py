from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import House,Room,Flat
from .serializers import HouseSerializer,RoomSerializer,FlatSerializer
from PIL import Image
# from .serializers import ImageSerializer
# from .models import Image


class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    @action(detail=False, methods=['GET'])
    def getresult(self, request, pk=None):
        house = House.objects.all()
        serializer = HouseSerializer(house, many=True)
        response = {'message': 'ok', 'result': serializer.data}
        return Response(response, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['POST'])
    def postresult(self, request, pk=None):
        # im1 = Image.open(request.data['img1'])
        # img11 = im1.resize((350,300))
        
        # im2 = Image.open(request.data['img2'])
        # img22 = im2.resize((350,300))
        
        # im3 = Image.open(request.data['img3'])
        # img33 = im3.resize((350,300))
        
        # im4 = Image.open(request.data['img4'])
        # img44 = im4.resize((350,300))
        
        house = House.objects.create(
            title = request.data['title'],
            img1=request.data['img1'],
            img2=request.data['img2'],
            img3=request.data['img3'],
            img4=request.data['img4'],
            bedroom = request.data['bedroom'],
            bathroom = request.data['bathroom'],
            balconies = request.data['balconies'],
            area = request.data['area'],
            furnished = request.data['furnished'],
            price = request.data['price'],
            additional_charge = request.data['additional_charge'],
            security_money = request.data['security_money'],
            locality = request.data['locality'],
            address = request.data['address'],
            city = request.data['city'],
            state = request.data['state'],
            pin = request.data['pin'],
            phone = request.data['phone'],
            available = request.data['available'],
            parking = request.data['parking'],
            agreement_duration = request.data['agreement_duration'],
            description = request.data['description']
        )
        serializer = HouseSerializer(house, many=False)
        response = {'message': 'model created', 'result': serializer.data}
        return Response(response, status=status.HTTP_200_OK)



class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    @action(detail=False, methods=['GET'])
    def getresult(self, request, pk=None):
        room = Room.objects.all()
        serializer = RoomSerializer(Room, many=True)
        response = {'message': 'ok', 'result': serializer.data}
        return Response(response, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['POST'])
    def postresult(self, request, pk=None):
        room = Room.objects.create(
            title = request.data['title'],
            img1=request.data['img1'],
            img2=request.data['img2'],
            img3=request.data['img3'],
            img4=request.data['img4'],
            bathroom = request.data['bathroom'],
            balconies = request.data['balconies'],
            area = request.data['area'],
            furnished = request.data['furnished'],
            ac = request.data['ac'],
            water = request.data['water'],
            electricity = request.data['electricity'],
            price = request.data['price'],
            additional_charge = request.data['additional_charge'],
            security_money = request.data['security_money'],
            locality = request.data['locality'],
            address = request.data['address'],
            city = request.data['city'],
            state = request.data['state'],
            pin = request.data['pin'],
            phone = request.data['phone'],
            available = request.data['available'],
            parking = request.data['parking'],
            agreement_duration = request.data['agreement_duration'],
            description = request.data['description']
        )
        serializer = RoomSerializer(Room, many=True)
        response = {'message': 'model created', 'result': serializer.data}
        return Response(response, status=status.HTTP_200_OK)
    


class FlatViewSet(viewsets.ModelViewSet):
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer
    @action(detail=False, methods=['GET'])
    def getresult(self, request, pk=None):
        Flat = Flat.objects.all()
        serializer = FlatSerializer(Flat, many=True)
        response = {'message': 'ok', 'result': serializer.data}
        return Response(response, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['POST'])
    def postresult(self, request, pk=None):
        Flat = Flat.objects.create(
            title = request.data['title'],
            img1=request.data['img1'],
            img2=request.data['img2'],
            img3=request.data['img3'],
            img4=request.data['img4'],
            floor = request.data['floor'],
            bedroom = request.data['bedroom'],
            bathroom = request.data['bathroom'],
            balconies = request.data['balconies'],
            area = request.data['area'],
            furnished = request.data['furnished'],
            price = request.data['price'],
            additional_charge = request.data['additional_charge'],
            security_money = request.data['security_money'],
            locality = request.data['locality'],
            address = request.data['address'],
            city = request.data['city'],
            state = request.data['state'],
            pin = request.data['pin'],
            phone = request.data['phone'],
            available = request.data['available'],
            parking = request.data['parking'],
            agreement_duration = request.data['agreement_duration'],
            description = request.data['description']
        )
        serializer = FlatSerializer(Flat, many=True)
        response = {'message': 'model created', 'result': serializer.data}
        return Response(response, status=status.HTTP_200_OK)
    


# test model to upload images

# class ImageViewSet(viewsets.ModelViewSet):
#     queryset = Image.objects.all()
#     serializer_class = ImageSerializer
#     @action(detail=False, methods=['GET'])
#     def resultget(self, request, pk=None):
#         try:
#             print("/api/images/resultget runs ")
#             image = Image.objects.all()
#             serializer = ImageSerializer(image, many=True)
#             response = {'message': 'ok', 'result': serializer.data}
#             return Response(response, status=status.HTTP_200_OK)
#         except:
#             response = {'message': 'not found'}
#             return Response(response, status=status.HTTP_404_NOT_FOUND)
        
#     @action(detail=False, methods=['POST'])
#     def resultpost(self, request, pk=None):
#         try:
#             # print(request.data['img1'])
#             image = Image.objects.create(img1=request.data['img1'],img2=request.data['img2'])
#             serializer = ImageSerializer(image, many=False)
#             response = {'message': 'model created', 'result': serializer.data}
#             return Response(response, status=status.HTTP_200_OK)
#         except:
#             response = {'message': 'not found'}
#             return Response(response, status=status.HTTP_404_NOT_FOUND)
    