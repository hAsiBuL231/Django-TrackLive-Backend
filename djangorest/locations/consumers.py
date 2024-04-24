import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class LocationConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = "location_updates"
        self.room_group_name = f"location_updates_{self.room_name}"

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        # Receive message from WebSocket
        text_data_json = json.loads(text_data)
        location = text_data_json['location']

        # Send location to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'location_update',
                'location': location
            }
        )

    # Receive location from room group
    def location_update(self, event):
        location = event['location']

        # Send location to WebSocket
        self.send(text_data=json.dumps({
            'location': location
        }))
