"""Fixtures for tests"""
import pytest

from orders.views import (get_deleted_rows, 
                            collect_changes, 
                            get_changes_in_gs)


@pytest.fixture
def supply_data_get_deleted_rows_1():
    data_1 = [{'Заказ №':1,'b':2},{'Заказ №':2,'b':1},{'Заказ №':3,'b':4},{'Заказ №':4,'b':4}]
    data_2 = [{'Заказ №':1,'b':2},{'Заказ №':3,'b':4},{'Заказ №':5,'b':4},{'Заказ №':6,'b':4},{'Заказ №':7,'b':4}]
    return get_deleted_rows(data_1, data_2)

@pytest.fixture
def supply_data_get_deleted_rows_2():
    data_1 = [{'Заказ №':1,'b':2},{'Заказ №':2,'b':1},{'Заказ №':3,'b':4},{'Заказ №':4,'b':4}]
    data_2 = [{'Заказ №':1,'b':2},{'Заказ №':2,'b':1}]
    return get_deleted_rows(data_1, data_2)

@pytest.fixture
def supply_data_get_deleted_rows_3():
    data_1 = [{'Заказ №':1,'b':2},{'Заказ №':2,'b':1},{'Заказ №':3,'b':4}]
    data_2 = [{'Заказ №':1,'b':2},{'Заказ №':2,'b':1},{'Заказ №':3,'b':4}]
    return get_deleted_rows(data_1, data_2)

@pytest.fixture
def supply_data_get_deleted_rows_4():
    data_1 = [{'Заказ №':1,'b':2},{'Заказ №':2,'b':1},{'Заказ №':3,'b':4}]
    data_2 = []
    return get_deleted_rows(data_1, data_2)

@pytest.fixture
def supply_data_collect_changes_1():
    data_1 = [{'Заказ №':1,'b':2},{'Заказ №':2,'b':1},{'Заказ №':3,'b':4}]
    data_2 = [{'Заказ №':4,'b':4}]
    deleted_rows = get_deleted_rows(data_1, data_2)
    return collect_changes(data_1, data_2, deleted_rows)

@pytest.fixture
def supply_data_collect_changes_2():
    data_1 = [{'Заказ №':1,'b':2},{'Заказ №':2,'b':1},{'Заказ №':3,'b':4}]
    data_2 = [{'Заказ №':4,'b':4},{'Заказ №':5,'b':4}]
    deleted_rows = get_deleted_rows(data_1, data_2)
    return collect_changes(data_1, data_2, deleted_rows)

@pytest.fixture
def supply_data_collect_changes_3():
    data_1 = [{'Заказ №':1,'b':2},{'Заказ №':2,'b':1},{'Заказ №':3,'b':4}]
    data_2 = [{'Заказ №':4,'b':4},{'Заказ №':5,'b':4},{'Заказ №':1,'b':3}, {'Заказ №':2,'b':2}]
    deleted_rows = get_deleted_rows(data_1, data_2)
    return collect_changes(data_1, data_2, deleted_rows)

@pytest.fixture
def supply_data_get_changes_in_gs_1():
    data_1 = [{'Заказ №':1,'b':2},{'Заказ №':2,'b':1},{'Заказ №':3,'b':4}]
    data_2 = [{'Заказ №':1,'b':2},{'Заказ №':2,'b':1},{'Заказ №':3,'b':4}]
    return get_changes_in_gs(data_1, data_2)

@pytest.fixture
def supply_data_get_changes_in_gs_2():
    data_1 = [{'Заказ №':1,'b':2},{'Заказ №':2,'b':1},{'Заказ №':3,'b':4}]
    data_2 = [{'Заказ №':1,'b':2},{'Заказ №':2,'b':1}]
    return get_changes_in_gs(data_1, data_2)

@pytest.fixture
def supply_data_get_changes_in_gs_3():
    data_1 = [{'Заказ №':1,'b':2},{'Заказ №':2,'b':1},{'Заказ №':3,'b':4}]
    data_2 = [{'Заказ №':1,'b':2},{'Заказ №':2,'b':1},{'Заказ №':3,'b':4}, {'Заказ №':4,'b':2}]
    return get_changes_in_gs(data_1, data_2)

@pytest.fixture
def supply_data_get_changes_in_gs_4():
    data_1 = [{'Заказ №':1,'b':2},{'Заказ №':2,'b':1},{'Заказ №':3,'b':4}]
    data_2 = [{'Заказ №':3,'b':4},{'Заказ №':7,'b':2},{'Заказ №':5,'b':2},{'Заказ №':6,'b':2}]
    return get_changes_in_gs(data_1, data_2)

@pytest.fixture
def supply_data_get_changes_in_gs_5():
    data_1 = [{'Заказ №':1,'b':2},{'Заказ №':2,'b':1},{'Заказ №':3,'b':4}]
    data_2 = [{'Заказ №':1,'b':2},{'Заказ №':2,'b':1},{'Заказ №':3,'b':66}]
    return get_changes_in_gs(data_1, data_2)

@pytest.fixture
def supply_data_get_changes_in_gs_6():
    data_1 = [{'Заказ №':1,'b':2},{'Заказ №':2,'b':1},{'Заказ №':3,'b':4}]
    data_2 = [{'Заказ №':1,'b':2},{'Заказ №':3,'b':66},]
    return get_changes_in_gs(data_1, data_2)

@pytest.fixture
def supply_data_get_changes_in_gs_7():
    data_1 = [{'Заказ №':1,'b':2},{'Заказ №':2,'b':1},{'Заказ №':3,'b':4}]
    data_2 = [{'Заказ №':1,'b':2},{'Заказ №':2,'b':1},{'Заказ №':3,'b':66},{'Заказ №':4,'b':2}]
    return get_changes_in_gs(data_1, data_2)

@pytest.fixture
def supply_data_get_changes_in_gs_8():
    data_1 = [{'Заказ №':1,'b':2},{'Заказ №':2,'b':1},{'Заказ №':3,'b':4}]
    data_2 = [{'Заказ №':4,'b':4},{'Заказ №':5,'b':4},{'Заказ №':1,'b':3}, {'Заказ №':2,'b':2}]
    return get_changes_in_gs(data_1, data_2)