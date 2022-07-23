def test_collect_changes_1(supply_data_collect_changes_1):
    assert {'added_rows':[{'Заказ №':4,'b':4}], 'updated_rows':[], 'deleted_rows': [{'Заказ №':1,'b':2},{'Заказ №':2,'b':1},{'Заказ №':3,'b':4}]} == supply_data_collect_changes_1

def test_collect_changes_2(supply_data_collect_changes_2):
    assert {'added_rows':[{'Заказ №':4,'b':4},{'Заказ №':5,'b':4}], 'updated_rows':[],'deleted_rows': [{'Заказ №':1,'b':2},{'Заказ №':2,'b':1},{'Заказ №':3,'b':4}]} == supply_data_collect_changes_2

def test_collect_changes_3(supply_data_collect_changes_3):
    assert {'added_rows':[{'Заказ №':4,'b':4},{'Заказ №':5,'b':4}], 'updated_rows':[{'Заказ №':1,'b':3}, {'Заказ №':2,'b':2}], 'deleted_rows': [{'Заказ №':3,'b':4}]} == supply_data_collect_changes_3
