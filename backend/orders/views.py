from rest_framework.response import Response
from rest_framework.decorators import api_view
from pydantic_model import Order
import pygsheets
import os
import requests
import xml.etree.ElementTree as ET


@api_view(['GET'])
def orders_list(request):
    if request.method == 'GET':
        wk1 = auth_to_gs()
        resp = requests.get('https://www.cbr.ru/scripts/XML_daily.asp')
        a = get_ruble_exchange_rate(ET.fromstring(resp.content))
        all = wk1.get_all_records()  
        c = add_ruble_price_field(all, a)   
        return Response({'data': gs})

def auth_to_gs():
    gs = pygsheets.authorize(service_file='./service_account_credentials.json')
    sh = gs.open_by_key(os.getenv('GS_KEY'))
    return sh[0]

def get_ruble_exchange_rate(exchange_rates) -> str:
    ruble_exchange_rate = [exchange_rate[4].text for exchange_rate in exchange_rates if exchange_rate.attrib.get('ID', '') == 'R01235'][0]
    return float(ruble_exchange_rate.replace(',','.'))

def add_ruble_price_field(gs, ruble_exchange_rate) -> list:
    for row in gs:
        row['стоимость, руб'] = row['стоимость,$'] * ruble_exchange_rate
    return gs