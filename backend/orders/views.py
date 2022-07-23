from datetime import datetime
from rest_framework.response import Response
from rest_framework.decorators import api_view

import pygsheets
import environ
import requests
import xml.etree.ElementTree as ET

import pytz
from django.conf import settings

from .models import Order

env = environ.Env()
environ.Env.read_env()

@api_view(['GET'])
def orders_list(request):
    if request.method == 'GET':
        wk1 = auth_to_gs()
        resp = requests.get('https://www.cbr.ru/scripts/XML_daily.asp')
        ruble_exchange_rate = get_ruble_exchange_rate(ET.fromstring(resp.content))
        gs = wk1.get_all_records()  
        gs_with_ruble_price_field = add_ruble_price_field(gs, ruble_exchange_rate)  
        # orders = Order.parse_raw(gs_with_ruble_price_field)
        save_data(gs_with_ruble_price_field)
        return Response({'data': gs})

def auth_to_gs():
    gs = pygsheets.authorize(service_file='./service_account_credentials.json')
    sh = gs.open_by_key(env('GS_KEY'))
    return sh[0]

def get_ruble_exchange_rate(exchange_rates: list) -> str:
    ruble_exchange_rate = [exchange_rate[4].text for exchange_rate in exchange_rates if exchange_rate.attrib.get('ID', '') == 'R01235'][0]
    return float(ruble_exchange_rate.replace(',','.'))

def add_ruble_price_field(gs, ruble_exchange_rate) -> list:
    for row in gs:
        row['стоимость, руб'] = row['стоимость,$'] * ruble_exchange_rate
    return gs

def save_data(gs_with_ruble_price_field: list):
    for row in gs_with_ruble_price_field:
        date = datetime.strptime(row.get('срок поставки'), '%d.%m.%Y')
        date = date.replace(tzinfo=pytz.timezone(settings.TIME_ZONE))
        order = Order(num=row.get('№'), order_num=row.get('заказ №'), 
                        dollar_price=row.get('стоимость,$'), ruble_price=row.get('стоимость, руб'), 
                        delivery_time=date)

        order.save()

def get_changes_in_gs(old_data, new_data):
    new_rows = find_new_rows(old_data, new_data)
    deleted_rows = check_dublicates(new_rows, old_data) #нужно написать условия для удаления из бд строк
    added_or_updated_rows = check_dublicates(new_rows, new_data) 

    updated_rows = check_updated_rows(added_or_updated_rows, old_data)
    added_rows = check_added_rows(updated_rows,new_rows)
    
    return new_rows

def find_new_rows(old_data: list, new_data: list) -> list:
    new_rows = []
    if len(old_data) < len(new_data):
        bigger = new_data
        smaller = old_data
    else:
        bigger = old_data
        smaller = new_data

    for row in bigger:
        if row not in smaller and len(smaller) !=0:
            new_rows.append(row)
    return new_rows

def check_dublicates(new_rows, old_rows) -> bool:
    return [new_row for new_row in new_rows if new_row in old_rows]

def check_updated_rows(added_or_updated_rows, old_rows):
    unique_field = 'Заказ №'
    updated_rows = []
    for added_or_updated_row in added_or_updated_rows:
        for old_row in old_rows:
            if added_or_updated_row.get(unique_field) == old_row.get(unique_field):
                updated_rows.append(added_or_updated_row)
    return updated_rows

def check_added_rows(updated_rows: list, new_rows: list) -> list:
    return [new_row for new_row in new_rows if new_row not in updated_rows]
