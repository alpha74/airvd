from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.exceptions import PermissionDenied, ValidationError

from device.models import Device, TemperatureReading, HumidityReading
from api.serializers import DeviceSerializer


"""
	- GET : Get all device details
	- POST : Add new device
"""
@api_view( ['GET','POST'] )
def apiDevice( request ):
	
	# Return list of all devices
	if( request.method == "GET" ):
		try:
			device_data = Device.objects.all()
			
		except Device.DoesNotExist:
			return Response( status = status.HTTP_404_NOT_FOUND )
		
	
		serializer = DeviceSerializer( device_data, many=True )
		return Response( serializer.data )
		
	
	# Create new device
	elif ( request.method == "POST" ):
		try:
			# Extract attributes
			payload = request.POST
		
			uid = payload["uid"]
			name = payload["name"]
			
			# Create new Device
			device_new = Device( uid = uid, name = name )
			
			Device.full_clean( device_new )
			
			device_new.save()
			
		
		except PermissionDenied as e:
			return Response( status = status.HTTP_401_BAD_REQUEST )
		
		except ValidationError as e:
			return Response( status = status.HTTP_409_CONFLICT )
	 

		return Response( status = status.HTTP_201_CREATED )
		

"""
	- GET : Get details of all devices
"""
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
		
