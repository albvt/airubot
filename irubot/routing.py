from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    url(r'^ws/irubot/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),
]
