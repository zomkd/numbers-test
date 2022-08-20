"""db data manipulate functions"""
from datetime import datetime

import pytz

from django.conf import settings

from .models import Order
from .config import *


def delete_rows_from_db(changes):
    """delete rows which was removed from new version of google table"""
    for deleted_data in changes.get('deleted_rows'):
        deleted_field = deleted_data.get(ORDER_NUM_FIELD)
        Order.objects.filter(order_num=deleted_field).delete()


def update_rows_from_db(changes):
    """update rows which was updated from new version of google table"""
    for updated_data in changes.get('updated_rows'):
        date = _change_date_format(updated_data)
        Order.objects.filter(
            order_num=updated_data.get(ORDER_NUM_FIELD)).update(
                dollar_price=updated_data.get(DOLLAR_PRICE_FIELD),
                ruble_price=updated_data.get(RUBLE_PRICE_FIELD),
                delivery_time=date)


def add_rows_from_db(changes):
    """add rows which was added from new version of google table"""
    for added_rows in changes.get('added_rows'):
        date = _change_date_format(added_rows)
        Order.objects.create(
            num=added_rows.get(NUM_FIELD), order_num=added_rows.get(ORDER_NUM_FIELD),
            dollar_price=added_rows.get(DOLLAR_PRICE_FIELD),
            ruble_price=added_rows.get(RUBLE_PRICE_FIELD), delivery_time=date)


def save_data(gs_with_ruble_price_field: list):
    """save data in db"""
    for row in gs_with_ruble_price_field:
        date = _change_date_format(row)
        order = Order(
            num=row.get(NUM_FIELD), order_num=row.get(ORDER_NUM_FIELD),
            dollar_price=row.get(DOLLAR_PRICE_FIELD), ruble_price=row.get(RUBLE_PRICE_FIELD),
            delivery_time=date)
        order.save()


def _change_date_format(data: dict):
    """change date from frontend to correct date format"""
    date = datetime.strptime(data.get(DELIVERY_TIME_FIELD), '%d.%m.%Y')
    return date.replace(tzinfo=pytz.timezone(settings.TIME_ZONE))
