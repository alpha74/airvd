from django.db import models
from django.utils import timezone

"""
	Device model:
		- uid : unique id of device
		- name : textual name of device
		- date_added : date when device was added
"""
class Device( models.Model ):
	uid = models.CharField( max_length = 12 )
	name = models.TextField()
	date_added = models.DateTimeField( default = timezone.now )
	
	def __str__( self ):
		return self.uid + " " + self.name

		
	class Meta:
		ordering = [ "uid" ]


"""
	Temperature Reading
		- uid : unique id of device
		- temperature : temperature reading in decimal
		- timestamp : timestamp when reading was made
"""
class TemperatureReading( models.Model ):
	uid = models.ForeignKey( Device, on_delete = models.CASCADE )
	temperature = models.DecimalField( decimal_places = 4, max_digits = 7 )
	timestamp = models.DateTimeField( default = timezone.now )
	
	def __str__( self ):
		return self.uid + " " + self.temperature

"""
	- uid : unique id of device
	- humidity : humidity reading in decimal
	- timestamp : timestamp when reading was made
"""
class HumidityReading( models.Model ):
	uid = models.ForeignKey( Device, on_delete = models.CASCADE )
	humidity = models.DecimalField( decimal_places = 2, max_digits = 5 )
	timestamp = models.DateTimeField( default = timezone.now )
	
	def __str__( self ):
		return self.uid + " " + self.humidity
	