
def test_find_new_rows_1(supply_data_find_new_rows_1):
    assert [] == supply_data_find_new_rows_1

def test_find_new_rows_2(supply_data_find_new_rows_2):
    assert [{'a':4,'b':4}] == supply_data_find_new_rows_2

def test_find_new_rows_3(supply_data_find_new_rows_3):
    assert [{'a':4,'b':4},{'a':5,'b':2}] == supply_data_find_new_rows_3

def test_find_new_rows_4(supply_data_find_new_rows_4):
    assert [{'a':3,'b':4}] == supply_data_find_new_rows_4

def test_find_new_rows_5(supply_data_find_new_rows_5):
    assert [] == supply_data_find_new_rows_5

def test_find_new_rows_6(supply_data_find_new_rows_6):
    assert [] == supply_data_find_new_rows_6

