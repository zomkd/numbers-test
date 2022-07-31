from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class OrderConsumer(WebsocketConsumer):
    def connect(self):
        async_to_sync(self.channel_layer.group_add)(
            "orders", self.channel_name
        )

        self.accept()

    def disconnect(self):
        async_to_sync(self.channel_layer.group_discard)

    def orders_order(self, event):
        self.send(text_data=event["text"])