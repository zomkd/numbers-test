from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import pygsheets
import requests

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Order
from .serializers import OrderSerializer

@api_view(['GET'])
def orders_list(request):
    if request.method == 'GET':
        gs = pygsheets.authorize(service_file='./service_account_credentials.json')
        sh = gs.open_by_key('1vgQcg_gxXXY4gzGI8bMTCYIgLmn8ZJNigdw68IT6oss')
        wk1 = sh[0]
        r = requests.get('https://www.cbr.ru/scripts/XML_daily.asp')
        all = wk1.get_all_records()      
        return Response({'data': gs})