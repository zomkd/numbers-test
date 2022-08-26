import { render, screen, cleanup } from '@testing-library/react'
import Table from '../Table'


test('test', () => {
    const theadData = ["№", "заказ №", "стоимость,$", "срок поставки", "стоимость, руб"]
    const total = [
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
    render(<Table
        theadData={theadData}
        data={total}
        rowsPerPage={rowsPerPage}
    />)
    const orderTableElement = screen.getByTestId('orders-table')
    expect(orderTableElement).toBeInTheDocument;
}) 