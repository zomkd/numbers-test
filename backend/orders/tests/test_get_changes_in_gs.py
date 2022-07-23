def test_check_get_changes_in_gs_1(supply_data_get_changes_in_gs_1):
    assert {'added_rows': [], 'deleted_rows': [], 'updated_rows': []} == supply_data_get_changes_in_gs_1

def test_check_get_changes_in_gs_2(supply_data_get_changes_in_gs_2):
    assert {'added_rows':[], 'updated_rows':[], 'deleted_rows': [{'Заказ №':3,'b':4}]} == supply_data_get_changes_in_gs_2

def test_check_get_changes_in_gs_3(supply_data_get_changes_in_gs_3):
    assert {'added_rows':[{'Заказ №':4,'b':2}], 'updated_rows':[], 'deleted_rows': []} == supply_data_get_changes_in_gs_3

def test_check_get_changes_in_gs_4(supply_data_get_changes_in_gs_4):
    assert {'added_rows':[{'Заказ №':7,'b':2},{'Заказ №':5,'b':2},{'Заказ №':6,'b':2}], 'updated_rows':[], 'deleted_rows': [{'Заказ №':1,'b':2},{'Заказ №':2,'b':1}]} == supply_data_get_changes_in_gs_4

def test_check_get_changes_in_gs_5(supply_data_get_changes_in_gs_5):
    assert {'added_rows':[], 'updated_rows':[{'Заказ №':3,'b':66}], 'deleted_rows': []} == supply_data_get_changes_in_gs_5

def test_check_get_changes_in_gs_6(supply_data_get_changes_in_gs_6):
    assert {'added_rows':[], 'updated_rows':[{'Заказ №':3,'b':66}], 'deleted_rows': [{'Заказ №':2,'b':1}]} == supply_data_get_changes_in_gs_6

def test_check_get_changes_in_gs_7(supply_data_get_changes_in_gs_7):
    assert {'added_rows':[{'Заказ №':4,'b':2}], 'updated_rows':[{'Заказ №':3,'b':66}], 'deleted_rows': []} == supply_data_get_changes_in_gs_7

def test_check_get_changes_in_gs_8(supply_data_get_changes_in_gs_8):
    assert {'added_rows':[{'Заказ №':4,'b':4},{'Заказ №':5,'b':4}], 'updated_rows':[{'Заказ №':1,'b':3},{'Заказ №':2,'b':2}], 'deleted_rows': [{'Заказ №':3,'b':4}]} == supply_data_get_changes_in_gs_8
