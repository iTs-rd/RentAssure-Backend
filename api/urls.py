from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import HouseViewSet,RoomViewSet,FlatViewSet
# from .views import ImageViewSet

router = routers.DefaultRouter()
router.register('house', HouseViewSet)
router.register('room', RoomViewSet)
router.register('flat', FlatViewSet)
# router.register('images', ImageViewSet)



urlpatterns = [
    path('', include(router.urls)),
]
