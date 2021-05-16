from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import DataViewSet,UserViewSet,DataViewSetList, UserViewSetPassword,ContactDataViewSet


router = routers.DefaultRouter()
router.register('viewuser', UserViewSet)
router.register('adduser', UserViewSetPassword)
router.register('data', DataViewSet)
router.register('datalist', DataViewSetList)
router.register('contact', ContactDataViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
