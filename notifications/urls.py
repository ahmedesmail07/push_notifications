from django.urls import path 
from .views import notification_view

urlpatterns = [
    path("",notification_view,name="notification")
]