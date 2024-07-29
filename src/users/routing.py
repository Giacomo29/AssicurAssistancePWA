from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path('ws/notifications/', consumers.Notification.as_asgi()),
]