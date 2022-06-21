from django.db import models


class Order(models.Model):
    order_num = models.PositiveIntegerField(verbose_name='Заказ №')
    dollar_price = models.PositiveIntegerField(verbose_name='Стоимость в долларах')
    ruble_price = models.PositiveIntegerField(verbose_name='Стоимость в рублях')
    delivery_time = models.DateTimeField(verbose_name='Срок поставки')

    def __str__(self):
        return self.order_num
        