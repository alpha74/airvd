from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.exceptions import PermissionDenied, ValidationError, ObjectDoesNotExist
from django.shortcuts import get_object_or_404

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
	- DELETE : Delete device
"""
@api_view( ['GET','DELETE',] )
def apiGetDeleteDevice( request, uid ):
	
	# Get device details
	if( request.method == "GET" ):	
		try:
		
			if( uid == "" ):
				device_data = Device.objects.all()
			else:
				device_data = get_object_or_404( Device, uid = uid )
			
		except Device.DoesNotExist:
			return Response( status = status.HTTP_404_NOT_FOUND )
			
		except ObjectDoesNotExist:
			return Response( status = status.HTTP_404_NOT_FOUND )
		
		if( request.method == "GET" ):
			serializer = DeviceSerializer( device_data, many=True )
			return Response( serializer.data )
			
	
	# Delete device
	elif( request.method == "DELETE" ):
		try:			
			# Get object with input uid
			device_del = get_object_or_404( Device, uid = uid )
			
			# Delete the object
			Device.objects.filter( uid = uid ).delete()
		
		except PermissionDenied as e:
			return Response( status = status.HTTP_401_BAD_REQUEST )
		
		except ObjectDoesNotExist as e:
			return Response( status = status.HTTP_404_NOT_FOUND )
	 
		if( request.method == "DELETE" ):
			return Response( status = status.HTTP_202_ACCEPTED )
			
