import { renderHook, render, screen } from '@testing-library/react';
import useTable from "../../hooks/useTable";
import TableFooter from '../Table/TableFooter'


test('table footer test', () => {
    const page = 1
    const setPage = 1
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

    render(<TableFooter
        slice={result.current.slice}
        page={page}
        setPage={setPage}
        range={result.current.range}
    />)
    const orderTableFooter = screen.getByTestId('table-footer')
    expect(orderTableFooter).toBeInTheDocument;
}) 
