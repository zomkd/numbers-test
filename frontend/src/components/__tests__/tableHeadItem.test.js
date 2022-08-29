import { render, screen } from '@testing-library/react';
import TableHeadItem from '../Table/TableHeadItem'


test('table head item test', () => {
    const theadData = ["№", "заказ №", "стоимость,$", "срок поставки", "стоимость, руб"]
    theadData.map((h) => {
        render( <TableHeadItem key={h} data={h} />)
      })
    const orderTableHeadItem = screen.queryAllByText('table-head-item')
    expect(orderTableHeadItem).toBeInTheDocument;
}) 
