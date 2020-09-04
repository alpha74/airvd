from django.db import models
from django.utils import timezone


class Device( models.Model ):
	uid = models.CharField( max_length = 12 )
	name = models.TextField()
	date_added = models.DateTimeField( default = timezone.now )
	
	def __str__( self ):
		return self.uid + " " + self.name

		
	class Meta:
		ordering = [ "uid" ]

