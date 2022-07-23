def test_get_deleted_rows_1(supply_data_get_deleted_rows_1):
    assert [{'Заказ №':2,'b':1},{'Заказ №':4,'b':4}] == supply_data_get_deleted_rows_1

def test_get_deleted_rows_2(supply_data_get_deleted_rows_2):
    assert [{'Заказ №':3,'b':4},{'Заказ №':4,'b':4}] == supply_data_get_deleted_rows_2

def test_get_deleted_rows_3(supply_data_get_deleted_rows_3):
    assert [] == supply_data_get_deleted_rows_3

def test_get_deleted_rows_4(supply_data_get_deleted_rows_4):
    assert [{'Заказ №':1,'b':2},{'Заказ №':2,'b':1},{'Заказ №':3,'b':4}] == supply_data_get_deleted_rows_4



