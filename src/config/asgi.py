"""
ASGI config for AssicurAssistance project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from users.consumers import Notification
import users.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

#application = get_asgi_application()


# ws_patterns = [
#     path("ws/notifications/", Notification.as_asgi()),
# ]


application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter(users.routing.websocket_urlpatterns),
})