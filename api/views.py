from rest_framework import viewsets,status
from rest_framework.response import Response
from .models import Data
from .serializers import DataSerializer,DataMiniSerializer
from PIL import Image

class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    def list(self, request, *args, **kwargs):
        response = {'message': 'You can\'t use GET method like this'}
        return Response(response, status=status.HTTP_406_NOT_ACCEPTABLE)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class DataViewSetList(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataMiniSerializer

    def create(self, request, *args, **kwargs):
        response = {'message': 'You can\'t use POST method like this'}
        return Response(response, status=status.HTTP_406_NOT_ACCEPTABLE)


    def list(self, request, *args, **kwargs):
        if 'start' in request.headers and 'end' in request.headers:
            queryset = Data.objects.filter(id__range=[request.headers['start'],request.headers['end']])
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            response = {'message': 'You can\'t use GET method like this'}
            return Response(response, status=status.HTTP_406_NOT_ACCEPTABLE)

    def retrieve(self, request, *args, **kwargs):
        response = {'message': 'You can\'t use GET method like this'}
        return Response(response, status=status.HTTP_406_NOT_ACCEPTABLE)
