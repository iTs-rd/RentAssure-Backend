from django.db.models.query import QuerySet
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import authentication_classes, permission_classes, action, api_view
from rest_framework.authtoken.models import Token
from .models import UserModel,DataModel
from .serializers import DataSerializer,DataMiniSerializer,UserSerializer
from .filters import DataFilter 



class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        token=request.headers['authorization'][6:]
        user = Token.objects.get(key=token).user.id
        queryset=UserModel.objects.get(id=user)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=False)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=False)

        response = {'message': 'ok','result':serializer.data}
        return Response(response)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}


        response = {'message': 'ok','result':serializer.data}
        return Response(response)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


class DataViewSet(viewsets.ModelViewSet):
    queryset = DataModel.objects.all()
    serializer_class = DataSerializer

    def list(self, request, *args, **kwargs):
        if 'start' in request.headers and 'end' in request.headers:
            a=int(request.headers['start'])
            b=int(request.headers['end'])
            queryset = DataModel.objects.all()
            myFilter = DataFilter(request.GET,queryset=queryset)
            queryset=myFilter.qs
            if(b != -1):
                queryset=queryset[a:b]
            # page = self.paginate_queryset(queryset)
            # if page is not None:
            #     serializer = DataMiniSerializer(page, many=True)
            #     return self.get_paginated_response(serializer.data)

            serializer = DataMiniSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            response = {'message': 'You can\'t use GET method like this'}
            return Response(response, status=status.HTTP_406_NOT_ACCEPTABLE)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        response = {'message': 'ok','result':serializer.data}
        return Response(response, status=status.HTTP_201_CREATED, headers=headers)




























class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes=()

    def list(self, request, *args, **kwargs):
        token=request.headers['authorization'][6:]
        user = Token.objects.get(key=token).user.id
        queryset=UserModel.objects.get(id=user)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=False)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=False)

        response = {'message': 'ok','result':serializer.data}
        return Response(response)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        # CHANGED
        response = {'message': 'ok','result':serializer.data}
        return Response(response)


    def retrieve(self, request, *args, **kwargs):
        response = {'message': 'You can\'t use GET method like this'}
        return Response(response, status=status.HTTP_406_NOT_ACCEPTABLE)

    def destroy(self, request, *args, **kwargs):
        response = {'message': 'You can\'t use DELETE method like this'}
        return Response(response, status=status.HTTP_406_NOT_ACCEPTABLE)


