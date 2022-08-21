"""Order consumer"""
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class OrderConsumer(WebsocketConsumer):
    """Order consumer"""

    def connect(self):
        """connect to websocket group orders"""
        async_to_sync(self.channel_layer.group_add)(
            "orders", self.channel_name
        )
        self.accept()

    def disconnect(self):
        """disconnect to websocket group orders"""
        async_to_sync(self.channel_layer.group_discard)

    def orders_order(self, event):
        """send message to websocket group orders"""
        self.send(text_data=event["text"])
