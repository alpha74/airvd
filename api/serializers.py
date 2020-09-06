from rest_framework import serializers
from device.models import Device, TemperatureReading, HumidityReading

# Serializer for class Device
class DeviceSerializer( serializers.ModelSerializer ):
	class Meta:
		model = Device
		fields = ( 'uid', 'name', 'date_added' )
		
		
# Serializer for class HumidityReading
class HumidityReadingSerializer( serializers.ModelSerializer ):
	class Meta:
		model = HumidityReading
		fields = ( 'humidity', 'timestamp' )


# Serializer for class TemperatureReading
class TemperatureReadingSerializer( serializers.ModelSerializer ):
	class Meta:
		model = TemperatureReading
		fields = ( 'temperature', 'timestamp' )