from asgiref.sync import async_to_sync
import json
from celery import shared_task
from channels.layers import get_channel_layer
from .gs_data import watching_gs


channel_layer = get_channel_layer()

@shared_task
def get_gs_data():
    order = watching_gs()
    async_to_sync(channel_layer.group_send)(
    "orders", {"type": "orders.order", "text": json.dumps(order)}
    )
    