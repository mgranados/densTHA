from rest_framework import serializers
from .models import Sensor, Heartbeat

class SensorSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Sensor
    fields = ['serial_number', 'uuid', 'online', 'metadata', 'created_at', 'last_heartbeat_date']
    
class HeartbeatSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Heartbeat
    fields = ['sensor', 'created_at', 'metadata']