import time
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.exceptions import PermissionDenied, ValidationError, ObjectDoesNotExist
from django.shortcuts import get_object_or_404

from device.models import Device, TemperatureReading, HumidityReading
from api.serializers import DeviceSerializer, HumidityReadingSerializer, TemperatureReadingSerializer


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
			return Response( status = status.HTTP_401_UNAUTHORIZED )
		
		
	 

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
			return Response( status = status.HTTP_401_UNAUTHORIZED )
		
		except ObjectDoesNotExist as e:
			return Response( status = status.HTTP_404_NOT_FOUND )
	 
		if( request.method == "DELETE" ):
			return Response( status = status.HTTP_202_ACCEPTED )
			


"""
	- GET : Get device readings
"""
@api_view( ['GET',] )
def apiGetReading( request, uid, parameter ):
	
	# Get Device readings
	if( request.method == "GET" ):
		try:
			payload = request.GET
			start_on_str = payload[ "start_on" ]
			end_on_str = payload[ "end_on" ]
			
			start_on_str = start_on_str.split("T")
			end_on_str = end_on_str.split("T")
			
			# Construct string for date
			start_on = start_on_str[0] + " " + start_on_str[1] + "Z"
			end_on = end_on_str[0] + " " + end_on_str[1] + "Z"
			
			# Check if the intended device exists or not		
			device = get_object_or_404( Device, uid = uid )
			
			#
			# For TemperatureReading
			#
			if( parameter == "temperature" ):
			
				# Get all readings of device
				device_readings = TemperatureReading.objects.filter( device = uid )				
				# Get device readings in range
				device_readings = device_readings.filter( timestamp__gte = start_on ).filter( timestamp__lte = end_on )
				# Order the readings				
				device_readings.order_by( "timestamp" )
				
				# Set serializer
				serializer_tp = TemperatureReadingSerializer( device_readings, many=True )
				
			
			#
			# For HumidityReading
			#
			elif( parameter == "humidity" ):
				print( "\n\n Temp" )
				# Get all readings of device
				device_readings = HumidityReading.objects.filter( device = uid )				
				# Get device readings in range
				device_readings = device_readings.filter( timestamp__gte = start_on ).filter( timestamp__lte = end_on )
				# Order the readings				
				device_readings.order_by( "timestamp" )
				
				# Set serializer
				serializer_hd = HumidityReadingSerializer( device_readings, many=True )
		
		
		except ValidationError:
			return Response( status = status.HTTP_409_CONFLICT )
		except PermissionDenied:
			return Response( status = status.HTTP_400_BAD_REQUEST )
		except TypeError as e:
			print( "\n\n " + str(e) + "\n\n" )
			return Response( status = status.HTTP_417_EXPECTATION_FAILED )
		except ObjectDoesNotExist:
			return Response( status = status.HTTP_404_NOT_FOUND )
		
		# Return the readings
		if( parameter == "temperature" ):
			return Response( serializer_tp.data )
		elif( parameter == "humidity" ):
			return Response( serializer_hd.data )
