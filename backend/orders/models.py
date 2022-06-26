from django.db import models


class Order(models.Model):
    num = models.PositiveIntegerField(verbose_name='№')
    order_num = models.PositiveIntegerField(verbose_name='Заказ №')
    dollar_price = models.PositiveIntegerField(verbose_name='Стоимость, $')
    ruble_price = models.PositiveIntegerField(verbose_name='Стоимость в руб.')
    delivery_time = models.DateTimeField(verbose_name='Срок поставки')

    def __str__(self):
        return self.order_num
