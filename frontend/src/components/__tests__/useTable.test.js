import { renderHook } from '@testing-library/react';
import useTable from "../../hooks/useTable";


test('useTable hook test', () => {
    const page = 1
    const data = [
        {
            "№": 1,
            'срок поставки': "12.06.2022",
            'заказ №': 121231123,
            'стоимость,$': 3,
            'стоимость, руб': 150,
        },
        {
            "№": 2,
            'срок поставки': "14.06.2022",
            'заказ №': 121123,
            'стоимость,$': 23,
            'стоимость, руб': 1250,
        },
        {
            "№": 3,
            'срок поставки': "16.06.2022",
            'заказ №': 121123,
            'стоимость,$': 23,
            'стоимость, руб': 1250,
        }
    ]
    const rowsPerPage = 2
    const { result } = renderHook(() => useTable(data, page, rowsPerPage))

    expect(result.current.range).toStrictEqual([1, 2])
})
