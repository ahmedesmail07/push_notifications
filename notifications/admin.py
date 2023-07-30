from email import message
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.urls import is_valid_path
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .models import Notification
from django.urls import path
# admin.site.register(Notification)

from django import forms
# Define a custom form for adding notifications
class SendNotificationForm(forms.Form):
    message = forms.CharField(label="Notification Message", max_length=200)

# Register the Notification model with the admin site
@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    # Specify the path to the custom add form template
    add_form_template = "admin/custom_add_form.html"

    # Override the add_view method to handle adding new notifications
    def add_view(self, request, form_url="", extra_context=None):
        # If the request method is POST, process the form data
        if request.method == "POST":
            # Create a new form instance with the POST data
            form = SendNotificationForm(request.POST)
            # If the form is valid, create a new Notification object
            if form.is_valid():
                message = form.cleaned_data["message"]
                notification = Notification.objects.create(message=message)
                channel_layer = get_channel_layer()
                async_to_sync(channel_layer.group_send)(
                    "notifications",
                    {
                        "type":"send_notification",
                        "message":message,
                    }
                )

                return HttpResponseRedirect("../{}/".format(notification.pk))
        else:
            # If the request method is not POST, create a new form instance
            form = SendNotificationForm()
            
        # Get the initial data for the form
        context = self.get_changeform_initial_data(request)
        # Add the form to the context dictionary
        context["form"] = form
        # Call the parent class's add_view method with the updated context
        return super().add_view(request, form_url, extra_context=context)
        
    def get_urls(self):
            urls = super().get_urls()
            custom_url = [
                path("send-notification/", self.admin_site.admin_view(self.add_view),\
                    name="send-notification"),
            ]
            return custom_url + urls