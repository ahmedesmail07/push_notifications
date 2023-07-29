import os

from channels.routing import ProtocolTypeRouter , URLRouter
from django import urls

from django.core.asgi import get_asgi_application

# It can not be above, the django application above is not contained in this file.
from . import urls

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")

application = ProtocolTypeRouter(
    {
        "http" : get_asgi_application(),
        "websocket" : URLRouter(urls.websocket_urlpatterns),
    }
)

