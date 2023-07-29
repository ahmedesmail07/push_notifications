from django.contrib import admin
from django.urls import path , include
from notifications.consumers import NotificationConsumer

urlpatterns = [
    path("admin/", admin.site.urls),
    path("notification/",include("notifications.urls"))
]

websocket_patterns = [
    # Endpoin of creating a web socket
    path("ws/notifications/", NotificationConsumer.as_asgi())
]