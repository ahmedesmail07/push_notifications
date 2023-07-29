from django.contrib import admin

from .models import Notification

# admin.site.register(Notification)

from django import forms

class SendNotificationForm(forms.Form):
    message = forms.CharField(label="Notification Message" , max_length= 200)

admin.site.register(Notification)

class NotificationAdmin(admin.ModelAdmin):
    pass
