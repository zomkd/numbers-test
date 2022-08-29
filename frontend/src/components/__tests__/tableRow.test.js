import { renderHook, render, screen } from '@testing-library/react';
import useTable from "../../hooks/useTable";
import TableRow from '../Table/TableRow'


test('table row test', () => {
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
    result.current.slice.map((el) => {
        render( <TableRow key={el['№']} data={el} />)
      })
    const orderTableRow = screen.queryAllByText('table-row')
    expect(orderTableRow).toBeInTheDocument;
}) 
