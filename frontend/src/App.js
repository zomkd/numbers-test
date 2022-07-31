import  React, { Component } from  'react'; 

import  OrdersService  from  './OrdersService';
import {w3cwebsocket as W3CWebSocket} from 'websocket';
import "./index.css";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend
} from "recharts";

const  ordersService  =  new  OrdersService();

class OrdersChart extends Component {
  constructor(props) {
    super(props);
    this.state  = {
      orders: [
        {
          'срок поставки': "12.06.2022",
          'заказ №': 121231123,
          'стоимость,$': 3,
          'стоимость, руб': 150,
          'общая цена': 64444,
          'общее': 4,
        },
        {
          'срок поставки': "14.06.2022",
          'заказ №': 121123,
          'стоимость,$': 23,
          'стоимость, руб': 1250,
          'общая цена': 44444,
          'общее': 14,
        },
        {
          'срок поставки': "16.06.2022",
          'заказ №': 121123,
          'стоимость,$': 23,
          'стоимость, руб': 1250,
          'общая цена': 44444,
          'общее': 14,
        }
      ],
    };
  }
  client = new W3CWebSocket('ws://127.0.0.1:8000/ws/orders/')
  componentDidMount() {
    var  self  =  this;
    this.client.onopen = () => {
      console.log('websucket')
    }
    this.client.onmessage = (gs_data) => {
      const dataFromSever = JSON.parse(gs_data.data);
      console.log(
        'asdasd'
      )
      if (dataFromSever) {
        console.log(dataFromSever)
        this.setState({orders: dataFromSever})
      }
    }
    // ordersService.getOrders().then(function (result) {
    //   console.log(result);
    //   self.setState({ orders:  result.data})
    // });
  }
  render () {
    return (
      <LineChart
        width={500}
        height={300}
        data={this.state.orders}
        margin={{
          top: 5,
          right: 30,
          left: 20,
          bottom: 5
        }}
      >
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="срок поставки" />
        <YAxis />
        <Tooltip />
        <Legend />
        <Line
          type="monotone"
          dataKey="общая цена"
          stroke="#8884d8"
          activeDot={{ r: 2 }}
        />
        <Line type="monotone" dataKey="total" stroke="#82ca9d" />
      </LineChart>
    );
  }
}

export default OrdersChart;
