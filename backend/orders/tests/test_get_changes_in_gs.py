from orders.config import ORDER_NUM_FIELD


def test_check_get_changes_in_gs_1(supply_data_get_changes_in_gs_1):
    assert {'added_rows': [], 'deleted_rows': [],
            'updated_rows': []} == supply_data_get_changes_in_gs_1


def test_check_get_changes_in_gs_2(supply_data_get_changes_in_gs_2):
    assert {'added_rows': [], 'updated_rows': [], 'deleted_rows': [
        {ORDER_NUM_FIELD: 3, 'b': 4}]} == supply_data_get_changes_in_gs_2


def test_check_get_changes_in_gs_3(supply_data_get_changes_in_gs_3):
    assert {'added_rows': [{ORDER_NUM_FIELD: 4, 'b': 2}], 'updated_rows': [
    ], 'deleted_rows': []} == supply_data_get_changes_in_gs_3


def test_check_get_changes_in_gs_4(supply_data_get_changes_in_gs_4):
    assert {'added_rows': [{ORDER_NUM_FIELD: 7, 'b': 2}, {ORDER_NUM_FIELD: 5, 'b': 2}, {ORDER_NUM_FIELD: 6, 'b': 2}], 'updated_rows': [
    ], 'deleted_rows': [{ORDER_NUM_FIELD: 1, 'b': 2}, {ORDER_NUM_FIELD: 2, 'b': 1}]} == supply_data_get_changes_in_gs_4


def test_check_get_changes_in_gs_5(supply_data_get_changes_in_gs_5):
    assert {'added_rows': [], 'updated_rows': [{ORDER_NUM_FIELD: 3, 'b': 66}],
            'deleted_rows': []} == supply_data_get_changes_in_gs_5


def test_check_get_changes_in_gs_6(supply_data_get_changes_in_gs_6):
    assert {'added_rows': [], 'updated_rows': [{ORDER_NUM_FIELD: 3, 'b': 66}],
            'deleted_rows': [{ORDER_NUM_FIELD: 2, 'b': 1}]} == supply_data_get_changes_in_gs_6


def test_check_get_changes_in_gs_7(supply_data_get_changes_in_gs_7):
    assert {'added_rows': [{ORDER_NUM_FIELD: 4, 'b': 2}], 'updated_rows': [
        {ORDER_NUM_FIELD: 3, 'b': 66}], 'deleted_rows': []} == supply_data_get_changes_in_gs_7


def test_check_get_changes_in_gs_8(supply_data_get_changes_in_gs_8):
    assert {'added_rows': [{ORDER_NUM_FIELD: 4, 'b': 4}, {ORDER_NUM_FIELD: 5, 'b': 4}], 'updated_rows': [{ORDER_NUM_FIELD: 1, 'b': 3}, {
        ORDER_NUM_FIELD: 2, 'b': 2}], 'deleted_rows': [{ORDER_NUM_FIELD: 3, 'b': 4}]} == supply_data_get_changes_in_gs_8
