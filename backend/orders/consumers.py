import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .tasks import get_gs_data
from celery.result import AsyncResult

class OrderConsumer(WebsocketConsumer):
    def connect(self):
        # async_to_sync(self.channel_layer.group_add)
        self.accept()
        orders_task = get_gs_data.delay()
        orders_task_result = AsyncResult(orders_task.id)
        self.send(text_data=json.dumps({
            'message': orders_task_result.get()
        }))

    def disconnect(self):
        async_to_sync(self.channel_layer.group_discard)

