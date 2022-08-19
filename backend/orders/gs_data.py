from datetime import datetime
from django.forms.models import model_to_dict

import pygsheets
import environ
import requests
import xml.etree.ElementTree as ET

import pytz
from django.conf import settings

from .models import Order
from .data_manipulate import *


env = environ.Env()
environ.Env.read_env()

ORDER_NUM_FIELD = 'заказ №'
NUM_FIELD = '№'
DOLLAR_PRICE_FIELD = 'стоимость,$'
RUBLE_PRICE_FIELD = 'стоимость, руб'
DELIVERY_TIME_FIELD = 'срок поставки'


def ttt():
    wk1 = auth_to_gs()
    gs = wk1.get_all_records()

    ruble_exchange_rate = get_ruble_exchange_rate()
    gs_with_ruble_price_field = add_ruble_price_field(
        gs, ruble_exchange_rate)
    db_data = extract_db_data()

    if len(db_data) == 0:
        save_data(gs_with_ruble_price_field)
    else:
        changes = get_changes_in_gs(db_data, gs_with_ruble_price_field[:])
        apply_changes(changes)
    total_price_with_each_day = count_each_day_total_price(
        gs_with_ruble_price_field)
    total_prices_list = get_total_prices_list(total_price_with_each_day)
    orders = {'data': gs_with_ruble_price_field, 'total': total_prices_list}
    return orders


def apply_changes(changes: list):
    if len(changes.get('added_rows', [])) != 0:
        add_rows_from_db(changes)
    if len(changes.get('update_rows', [])) != 0:
        update_rows_from_db(changes)
    if len(changes.get('delete_rows', [])) != 0:
        delete_rows_from_db(changes)


def get_ruble_exchange_rate():
    url = 'https://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(url)
    exchange_rates = ET.fromstring(response.content)
    ruble_exchange_rate = [
        exchange_rate[4].text for exchange_rate in exchange_rates if exchange_rate.attrib.get('ID', '') == 'R01235'][0]
    return float(ruble_exchange_rate.replace(',', '.'))


def watching_gs():
    gs_with_ruble_price_field = []
    wk1 = auth_to_gs()
    resp = requests.get('https://www.cbr.ru/scripts/XML_daily.asp')
    ruble_exchange_rate = get_ruble_exchange_rate()
    if Order.objects.count() == 0:
        gs = wk1.get_all_records()
        gs_with_ruble_price_field = add_ruble_price_field(
            gs, ruble_exchange_rate)
        save_data(gs_with_ruble_price_field)
    else:
        db_data = extract_db_data()
        gs_new = wk1.get_all_records()
        gs_with_ruble_price_field = add_ruble_price_field(
            gs_new, ruble_exchange_rate)
        changes = get_changes_in_gs(db_data, gs_with_ruble_price_field[:])
        delete_rows_from_db(changes)
        add_rows_from_db(changes)
        update_rows_from_db(changes)
    total_price = count_each_day_total_price(gs_with_ruble_price_field)
    total_prices_list = get_total_prices_list(total_price)
    orders = {'data': gs_with_ruble_price_field, 'total': total_prices_list}
    return orders


def auth_to_gs():
    gs = pygsheets.authorize(service_file='./service_account_credentials.json')
    sh = gs.open_by_key(env('GS_KEY'))
    return sh[0]


# def get_ruble_exchange_rate(exchange_rates: list) -> str:
#     ruble_exchange_rate = [
#         exchange_rate[4].text for exchange_rate in exchange_rates if exchange_rate.attrib.get('ID', '') == 'R01235'][0]
#     return float(ruble_exchange_rate.replace(',', '.'))


def add_ruble_price_field(gs, ruble_exchange_rate) -> list:
    for row in gs:
        row['стоимость, руб'] = row['стоимость,$'] * ruble_exchange_rate
    return gs


def change_date_format(data: dict):
    date = datetime.strptime(data.get('срок поставки'), '%d.%m.%Y')
    return date.replace(tzinfo=pytz.timezone(settings.TIME_ZONE))


def save_data(gs_with_ruble_price_field: list):
    for row in gs_with_ruble_price_field:
        date = change_date_format(row)
        order = Order(num=row.get('№'), order_num=row.get('заказ №'),
                      dollar_price=row.get('стоимость,$'), ruble_price=row.get('стоимость, руб'),
                      delivery_time=date)
        order.save()


def get_changes_in_gs(db_data: list, new_rows: list) -> list:
    changes = {}
    if has_new_rows:
        deleted_rows = get_deleted_rows(db_data, new_rows)
        changes = collect_changes(db_data, new_rows, deleted_rows)
    return changes


def has_new_rows(db_data: list, new_rows: list) -> bool:
    for new_row in new_rows:
        if new_row not in db_data:
            return True
    return False


def get_deleted_rows(db_data: list, new_rows: list) -> list:
    deleted_rows = []
    for db_row in db_data:
        if db_row in new_rows:
            new_rows.remove(db_row)
        else:
            deleted_rows.append(db_row)
    return deleted_rows


def collect_changes(db_data: list, new_rows: list, deleted_rows) -> list:
    updated_rows = []
    deleted = []
    added_rows = new_rows[:]
    for new_row in new_rows:
        for db_row in db_data:
            if new_row.get(ORDER_NUM_FIELD) == db_row.get(ORDER_NUM_FIELD):
                updated_rows.append(new_row)
                added_rows.remove(new_row)

    deleted = clean_up_deleted_rows(updated_rows, deleted_rows)
    return {'added_rows': added_rows, 'updated_rows': updated_rows, 'deleted_rows': deleted}


def clean_up_deleted_rows(updated_rows, old_deleted_rows: list):
    deleted_rows = old_deleted_rows[:]
    for updated_row in updated_rows:
        for deleted_row in old_deleted_rows:
            if deleted_row[ORDER_NUM_FIELD] == updated_row[ORDER_NUM_FIELD]:
                deleted_rows.remove(deleted_row)
    return deleted_rows


def delete_rows_from_db(changes):
    for deleted_data in changes.get('deleted_rows'):
        deleted_field = deleted_data.get(ORDER_NUM_FIELD)
        Order.objects.filter(order_num=deleted_field).delete()


def update_rows_from_db(changes):
    for updated_data in changes.get('updated_rows'):
        date = change_date_format(updated_data)
        Order.objects.filter(order_num=updated_data.get(ORDER_NUM_FIELD)).update(dollar_price=updated_data.get(DOLLAR_PRICE_FIELD),
                                                                                 ruble_price=updated_data.get(RUBLE_PRICE_FIELD), delivery_time=date)


def add_rows_from_db(changes):
    for added_rows in changes.get('added_rows'):
        date = change_date_format(added_rows)
        Order.objects.create(num=added_rows.get(NUM_FIELD), order_num=added_rows.get(ORDER_NUM_FIELD), dollar_price=added_rows.get(DOLLAR_PRICE_FIELD),
                             ruble_price=added_rows.get(RUBLE_PRICE_FIELD), delivery_time=date)


# def db_obj_to_dict(db_objs):
#     db_dict = []
#     for db_obj in list(db_objs):
#         db_data = model_to_dict(db_obj)
#         db_data['delivery_time'] = db_data.get(
#             'delivery_time').strftime('%d.%m.%Y')
#         db_dict.append(db_data)
#     return db_dict


def extract_db_data():
    db_orders = list(Order.objects.all())
    orders = []
    for db_order in db_orders:
        order = {}
        db_order = model_to_dict(db_order)
        order[NUM_FIELD] = db_order.get('num')
        order[ORDER_NUM_FIELD] = db_order.get('order_num')
        order[DOLLAR_PRICE_FIELD] = db_order.get('dollar_price')
        order[RUBLE_PRICE_FIELD] = db_order.get('ruble_price')
        order[DELIVERY_TIME_FIELD] = db_order.get(
            'delivery_time').strftime('%d.%m.%Y')
        orders.append(order)
    return orders


def count_each_day_total_price(orders: list) -> dict:
    total_prices_with_each_day = {}
    for order in orders:
        if order[DELIVERY_TIME_FIELD] not in total_prices_with_each_day:
            total_prices_with_each_day[order[DELIVERY_TIME_FIELD]
                                       ] = order[DOLLAR_PRICE_FIELD]
        else:
            total_prices_with_each_day[order[DELIVERY_TIME_FIELD]
                                       ] += order[DOLLAR_PRICE_FIELD]
    return total_prices_with_each_day


def get_total_prices_list(total_prices_with_each_day: dict) -> list:
    total_prices_list = []
    for date, total in total_prices_with_each_day.items():
        total_price = {}
        total_price[DELIVERY_TIME_FIELD] = date
        total_price['общая цена'] = total
        total_prices_list.append(total_price)
    return total_prices_list
