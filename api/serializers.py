from rest_framework import serializers
from device.models import Device, TemperatureReading, HumidityReading


class DeviceSerializer( serializers.ModelSerializer ):
	class Meta:
		model = Device
		fields = ( 'uid', 'name', 'date_added' )