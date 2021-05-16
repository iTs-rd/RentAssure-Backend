from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import UserModel,DataModel
from .serializers import DataSerializer,DataMiniSerializer,UserSerializer,UserSerializerPassword
from .filters import DataFilter 
from rest_framework.settings import api_settings



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




class DataViewSetList(viewsets.ModelViewSet):
    queryset = DataModel.objects.all()
    serializer_class = DataMiniSerializer

    def create(self, request, *args, **kwargs):
        response = {'message': 'You can\'t use POST method like this'}
        return Response(response, status=status.HTTP_406_NOT_ACCEPTABLE)


    def list(self, request, *args, **kwargs):
        if 'start' in request.headers and 'end' in request.headers:
            a=int(request.headers['start'])
            b=int(request.headers['end'])
            queryset = DataModel.objects.all()
            myFilter = DataFilter(request.GET,queryset=queryset)
            queryset=myFilter.qs
            if(b != -1):
                queryset=queryset[a:b]
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            response = {'message': 'You can\'t use GET method like this'}
            return Response(response, status=status.HTTP_406_NOT_ACCEPTABLE)

    def retrieve(self, request, *args, **kwargs):
        response = {'message': 'You can\'t use GET method like this'}
        return Response(response, status=status.HTTP_406_NOT_ACCEPTABLE)

    def update(self, request, *args, **kwargs):
        response = {'message': 'You can\'t use PUT method like this'}
        return Response(response, status=status.HTTP_406_NOT_ACCEPTABLE)

    def destroy(self, request, *args, **kwargs):
        response = {'message': 'You can\'t use DELETE method like this'}
        return Response(response, status=status.HTTP_406_NOT_ACCEPTABLE)

