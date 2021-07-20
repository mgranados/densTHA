from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'sensors', views.SensorViewSet)
router.register(r'hearbeats', views.HeartbeatViewSet)

urlpatterns = [
  path('', include(router.urls)),
]