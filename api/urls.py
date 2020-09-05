from django.urls import path
from api.views import apiAllDevice, apiDetailDevice

app_name = "airvd"

urlpatterns = [
	path ( "", apiAllDevice ),
	path( "<str:uid>/", apiDetailDevice ),
]
