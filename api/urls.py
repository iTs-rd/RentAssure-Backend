from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import DataViewSet, DataViewSetList, ContactDataViewSet


router = routers.DefaultRouter()
router.register('data', DataViewSet)
router.register('datalist', DataViewSetList)
router.register('contact', ContactDataViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
