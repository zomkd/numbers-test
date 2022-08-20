from orders.config import ORDER_NUM_FIELD


def test_collect_changes_1(supply_data_collect_changes_1):
    assert {'added_rows': [{ORDER_NUM_FIELD: 4, 'b': 4}], 'updated_rows': [], 'deleted_rows': [
        {ORDER_NUM_FIELD: 1, 'b': 2}, {ORDER_NUM_FIELD: 2, 'b': 1}, {ORDER_NUM_FIELD: 3, 'b': 4}]} == supply_data_collect_changes_1


def test_collect_changes_2(supply_data_collect_changes_2):
    assert {'added_rows': [{ORDER_NUM_FIELD: 4, 'b': 4}, {ORDER_NUM_FIELD: 5, 'b': 4}], 'updated_rows': [], 'deleted_rows': [
        {ORDER_NUM_FIELD: 1, 'b': 2}, {ORDER_NUM_FIELD: 2, 'b': 1}, {ORDER_NUM_FIELD: 3, 'b': 4}]} == supply_data_collect_changes_2


def test_collect_changes_3(supply_data_collect_changes_3):
    assert {'added_rows': [{ORDER_NUM_FIELD: 4, 'b': 4}, {ORDER_NUM_FIELD: 5, 'b': 4}], 'updated_rows': [{ORDER_NUM_FIELD: 1, 'b': 3}, {
        ORDER_NUM_FIELD: 2, 'b': 2}], 'deleted_rows': [{ORDER_NUM_FIELD: 3, 'b': 4}]} == supply_data_collect_changes_3
