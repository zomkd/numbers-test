def test_check_updated_rows_1(supply_data_check_updated_rows_1):
    assert [{'Заказ №':1,'b':4}] == supply_data_check_updated_rows_1

def test_check_updated_rows_2(supply_data_check_updated_rows_2):
    assert [{'Заказ №':1,'b':4},{'Заказ №':5,'b':4}] == supply_data_check_updated_rows_2