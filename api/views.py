from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import UserModel,DataModel,ContactData
from .serializers import DataSerializer,DataMiniSerializer,UserSerializer,UserSerializerPassword,ContactDataSerializer
from .filters import DataFilter 

from .add_data import add_data
add_data()


class UserViewSetPassword(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializerPassword

    def retrieve(self, request, *args, **kwargs):
        response = {'message': 'You can\'t use GET method like this'}
        return Response(response, status=status.HTTP_406_NOT_ACCEPTABLE)

    def list(self, request, *args, **kwargs):
        response = {'message': 'You can\'t use GET method like this'}
        return Response(response, status=status.HTTP_406_NOT_ACCEPTABLE)

    def update(self, request, *args, **kwargs):
        response = {'message': 'You can\'t use PUT method like this'}
        return Response(response, status=status.HTTP_406_NOT_ACCEPTABLE)

    def destroy(self, request, *args, **kwargs):
        response = {'message': 'You can\'t use DELETE method like this'}
        return Response(response, status=status.HTTP_406_NOT_ACCEPTABLE)


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, )

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

    def create(self, request, *args, **kwargs):
        response = {'message': 'You can\'t use POST method like this'}
        return Response(response, status=status.HTTP_406_NOT_ACCEPTABLE)

    def retrieve(self, request, *args, **kwargs):
        response = {'message': 'You can\'t use GET method like this'}
        return Response(response, status=status.HTTP_406_NOT_ACCEPTABLE)

    def destroy(self, request, *args, **kwargs):
        response = {'message': 'You can\'t use DELETE method like this'}
        return Response(response, status=status.HTTP_406_NOT_ACCEPTABLE)


class DataViewSet(viewsets.ModelViewSet):
    queryset = DataModel.objects.all()
    serializer_class = DataSerializer
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication, )

    def list(self, request, *args, **kwargs):
        response = {'message': 'You can\'t use GET method like this'}
        return Response(response, status=status.HTTP_406_NOT_ACCEPTABLE)

    def create(self, request, *args, **kwargs):
        # CHANGED
        token=request.headers['authorization'][6:]
        user = Token.objects.get(key=token).user.id
        if request.data['user'] != str(user):
            response = {'message': 'Unauthorized user'}
            return Response(response, status=status.HTTP_401_UNAUTHORIZED)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        response = {'message': 'ok','result':serializer.data}
        return Response(response, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        token=request.headers['authorization'][6:]
        user = Token.objects.get(key=token).user.id
        if request.data['user'] != str(user):
            response = {'message': 'Unauthorized user'}
            return Response(response, status=status.HTTP_401_UNAUTHORIZED)
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

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        token=request.headers['authorization'][6:]
        userId = Token.objects.get(key=token).user.id
        if instance.user.id != userId:
            response = {'message': 'Unauthorized user'}
            return Response(response, status=status.HTTP_401_UNAUTHORIZED)
        self.perform_destroy(instance)
        response = {'message': 'ok'}
        return Response(response, status=status.HTTP_204_NO_CONTENT)


class DataViewSetList(viewsets.ModelViewSet):
    queryset = DataModel.objects.all()
    serializer_class = DataMiniSerializer

    def create(self, request, *args, **kwargs):
        response = {'message': 'You can\'t use POST method like this'}
        return Response(response, status=status.HTTP_406_NOT_ACCEPTABLE)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        myFilter = DataFilter(request.GET,queryset=queryset)
        queryset=myFilter.qs
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        response = {'message': 'You can\'t use GET method like this'}
        return Response(response, status=status.HTTP_406_NOT_ACCEPTABLE)

    def update(self, request, *args, **kwargs):
        response = {'message': 'You can\'t use PUT method like this'}
        return Response(response, status=status.HTTP_406_NOT_ACCEPTABLE)

    def destroy(self, request, *args, **kwargs):
        response = {'message': 'You can\'t use DELETE method like this'}
        return Response(response, status=status.HTTP_406_NOT_ACCEPTABLE)


class ContactDataViewSet(viewsets.ModelViewSet):
    queryset = ContactData.objects.all()
    serializer_class = ContactDataSerializer