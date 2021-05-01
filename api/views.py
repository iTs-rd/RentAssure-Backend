from rest_framework import viewsets,status
from rest_framework.response import Response
from .models import Data
from .serializers import DataSerializer,DataMiniSerializer
from PIL import Image


class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer

    def list(self, request, *args, **kwargs):
        if 'start' in request.headers and 'end' in request.headers:
            queryset = Data.objects.filter(id__range=[request.headers['start'],request.headers['end']])
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = DataMiniSerializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = DataMiniSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            response = {'message': 'You can\'t use GET method like this'}
            return Response(response, status=status.HTTP_406_NOT_ACCEPTABLE)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = DataSerializer(instance)
        return Response(serializer.data)