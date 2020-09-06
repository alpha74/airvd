from django.urls import path
from api.views import apiDevice, apiGetDeleteDevice, apiGetReading

app_name = "airvd"

urlpatterns = [
	path ( "", apiDevice ),
	path( "<str:uid>", apiGetDeleteDevice ),
	path( "<str:uid>/readings/<str:parameter>/", apiGetReading )
]
