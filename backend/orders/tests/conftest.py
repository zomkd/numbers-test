"""Fixtures for tests"""
import pytest
from orders.views import (find_new_rows, 
                            check_dublicates,
                            check_updated_rows,)


@pytest.fixture
def supply_data_find_new_rows_1():
    data_1 = [{'a':1,'b':2},{'a':2,'b':1},{'a':3,'b':4}]
    data_2 = [{'a':1,'b':2},{'a':2,'b':1},{'a':3,'b':4}]
    return find_new_rows(data_1,data_2)

@pytest.fixture
def supply_data_find_new_rows_2():
    data_1 = [{'a':1,'b':2},{'a':2,'b':1},{'a':3,'b':4}]
    data_2 = [{'a':1,'b':2},{'a':2,'b':1},{'a':3,'b':4},{'a':4,'b':4}]
    return find_new_rows(data_1,data_2)

@pytest.fixture
def supply_data_find_new_rows_3():
    data_1 = [{'a':1,'b':2},{'a':2,'b':1},{'a':3,'b':4}]
    data_2 = [{'a':1,'b':2},{'a':2,'b':1},{'a':3,'b':4},{'a':4,'b':4},{'a':5,'b':2}]
    return find_new_rows(data_1,data_2)

@pytest.fixture
def supply_data_find_new_rows_4():
    data_1 = [{'a':1,'b':2},{'a':2,'b':1},{'a':3,'b':4}]
    data_2 = [{'a':1,'b':2},{'a':2,'b':1}]
    return find_new_rows(data_2,data_1)

@pytest.fixture
def supply_data_find_new_rows_5():
    data_1 = [{'a':1,'b':2},{'a':2,'b':1},{'a':3,'b':4}]
    data_2 = []
    return find_new_rows(data_2, data_1)


@pytest.fixture
def supply_data_find_new_rows_6():
    data_1 = []
    data_2 = []
    return find_new_rows(data_2, data_1)

@pytest.fixture
def supply_data_check_dublicates_1():
    data_1 = [{'a':1,'b':2},{'a':2,'b':1},{'a':3,'b':4}]
    data_2 = [{'a':1,'b':2},{'a':2,'b':1},{'a':3,'b':4}]
    return check_dublicates(data_1, data_2)

@pytest.fixture
def supply_data_check_dublicates_2():
    data_1 = [{'a':1,'b':4},{'a':2,'b':4},{'a':3,'b':6}]
    data_2 = [{'a':1,'b':2},{'a':2,'b':1},{'a':3,'b':4}]
    return check_dublicates(data_1, data_2)

@pytest.fixture
def supply_data_check_dublicates_3():
    data_1 = [{'a':1,'b':4},{'a':2,'b':1},{'a':3,'b':6}]
    data_2 = [{'a':1,'b':2},{'a':2,'b':1},{'a':3,'b':4}]
    return check_dublicates(data_1, data_2)

@pytest.fixture
def supply_data_check_updated_rows_1():
    data_1 = [{'Заказ №':1,'b':4},{'Заказ №':2,'b':1},{'Заказ №':3,'b':6}]
    data_2 = [{'Заказ №':1,'b':2},{'Заказ №':5,'b':1},{'Заказ №':6,'b':4}]
    return check_updated_rows(data_1, data_2)
