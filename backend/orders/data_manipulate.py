from .models import Order

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