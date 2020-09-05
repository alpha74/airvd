from django.urls import path
from api.views import apiDevice, apiGetDeleteDevice

app_name = "airvd"

urlpatterns = [
	path ( "", apiDevice ),
	path( "<str:uid>", apiGetDeleteDevice ),
]
