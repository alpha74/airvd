from django.urls import path
from api.views import apiDevice, apiDetailDevice

app_name = "airvd"

urlpatterns = [
	path ( "", apiDevice ),
	path( "<str:uid>/", apiDetailDevice ),
]
