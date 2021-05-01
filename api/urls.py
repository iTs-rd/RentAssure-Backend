from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import DataViewSet


router = routers.DefaultRouter()
router.register('data', DataViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
