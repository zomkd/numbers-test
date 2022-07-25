import imp
from celery import shared_task
from .gs_data import watching_gs

@shared_task
def get_gs_data():
    gs_data = watching_gs()
    return gs_data
    