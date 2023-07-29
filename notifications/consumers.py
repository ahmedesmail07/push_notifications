import json
from django.template import Template , Context
from channels.generic.websocket import AsyncWebsocketConsumer

# Define a WebSocket consumer class that inherits from AsyncWebsocketConsumer
class NotificationConsumer(AsyncWebsocketConsumer):

    # Define a method to handle WebSocket connections
    async def connect(self):
        # Accept the WebSocket connection
        await self.accept()
        # Add the current channel to the "notifications" group
        await self.channel_layer.group_add("notifications",self.channel_name)

    # Define a method to handle WebSocket disconnections
    async def disconnect(self,close_code):
        # Remove the current channel from the "notifications" group
        await self.channel_layer.group_discard("notifications",self.channel_name)
    
    # Define a method to handle sending notifications to clients
    async def send_notification(self,event):
        # Extract the message from the event dictionary
        message = event["message"]

        # Define a Django template for rendering the notification HTML
        template = Template('<div class = "notification"><p>{{message}}</p></div>')
        # Define a context for the template with the message as a variable
        context = Context({"message":message})
        # Render the notification HTML using the template and context
        rendered_notification = template.render(context)

        # Send the rendered notification to the client as a JSON-encoded dictionary
        await self.send(    
            text_data=json.dumps(
            {
                "type":"notification",
                "message": rendered_notification
            }
            )
        )