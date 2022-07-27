import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .tasks import get_gs_data

class OrderConsumer(WebsocketConsumer):
    def connect(self):
        # async_to_sync(self.channel_layer.group_add)
        self.accept()
        orders = get_gs_data.delay()
        self.send(text_data=json.dumps({
            'message': orders
        }))

    def disconnect(self):
        async_to_sync(self.channel_layer.group_discard)

