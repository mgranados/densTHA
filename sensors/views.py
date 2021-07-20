from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import HeartbeatSerializer
from .serializers import SensorSerializer
from .models import Heartbeat
from .models import Sensor
# Create your views here.
def index(request):
  return HttpResponse("Hello sensors")
  
class SensorViewSet(viewsets.ModelViewSet):
  queryset = Sensor.objects.all().order_by('created_at')
  serializer_class = SensorSerializer
  
class HeartbeatViewSet(viewsets.ModelViewSet):
  queryset = Heartbeat.objects.all()
  serializer_class = HeartbeatSerializer