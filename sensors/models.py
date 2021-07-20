from django.db import models

# Expose an endpoint that can receive "heartbeats" indicating that the sensor is alive and checking in
# Expose an endpoint that can check whether or not a sensor is currently online
class Sensor(models.Model):
  serial_number = models.CharField(max_length=50)
  uuid = models.UUIDField()
  online = models.BooleanField(default=False)
  metadata = models.JSONField()
  created_at = models.DateField(auto_now=True)
  last_heartbeat_date = models.DateTimeField()
  
class Heartbeat(models.Model):
  sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now=True)
  metadata = models.JSONField