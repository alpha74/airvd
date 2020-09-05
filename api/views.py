from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from device.models import Device, TemperatureReading, HumidityReading
from api.serializers import DeviceSerializer



# Get details of all devices
@api_view( ['GET',] )
def apiAllDevice( request ):

	try:
		device_data = Device.objects.all()
		
	except Device.DoesNotExist:
		return Response( status = status.HTTP_404_NOT_FOUND )
	
	if( request.method == "GET" ):
		serializer = DeviceSerializer( device_data, many=True )
		return Response( serializer.data )
		

# Get detail of devices
@api_view( ['GET',] )
def apiDetailDevice( request, uid ):

	try:
		if( uid == "" ):
			device_data = Device.objects.all()
		else:
			device_data = Device.objects.filter( uid = uid )
		
	except Device.DoesNotExist:
		return Response( status = status.HTTP_404_NOT_FOUND )
		
	
	if( request.method == "GET" ):
		serializer = DeviceSerializer( device_data, many=True )
		return Response( serializer.data )
