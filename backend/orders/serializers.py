from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('num','order_num', 'dollar_price', 'ruble_price', 'delivery_time')
