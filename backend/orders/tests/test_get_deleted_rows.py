from orders.config import ORDER_NUM_FIELD


def test_get_deleted_rows_1(supply_data_get_deleted_rows_1):
    assert [{ORDER_NUM_FIELD: 2, 'b': 1}, {
        ORDER_NUM_FIELD: 4, 'b': 4}] == supply_data_get_deleted_rows_1


def test_get_deleted_rows_2(supply_data_get_deleted_rows_2):
    assert [{ORDER_NUM_FIELD: 3, 'b': 4}, {
        ORDER_NUM_FIELD: 4, 'b': 4}] == supply_data_get_deleted_rows_2


def test_get_deleted_rows_3(supply_data_get_deleted_rows_3):
    assert [] == supply_data_get_deleted_rows_3


def test_get_deleted_rows_4(supply_data_get_deleted_rows_4):
    assert [{ORDER_NUM_FIELD: 1, 'b': 2}, {ORDER_NUM_FIELD: 2, 'b': 1}, {
        ORDER_NUM_FIELD: 3, 'b': 4}] == supply_data_get_deleted_rows_4
