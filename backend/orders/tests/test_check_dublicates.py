def test_check_dublicates_1(supply_data_check_dublicates_1):
    assert [{'a':1,'b':2},{'a':2,'b':1},{'a':3,'b':4}] == supply_data_check_dublicates_1

def test_check_dublicates_2(supply_data_check_dublicates_2):
    assert [] == supply_data_check_dublicates_2

def test_check_dublicates_3(supply_data_check_dublicates_3):
    assert [{'a':2,'b':1}] == supply_data_check_dublicates_3