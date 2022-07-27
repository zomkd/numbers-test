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
          delivery_time: "12.06.2022",
          order_num: 121231123,
          dollar_price: 3,
          ruble_price: 150,
          general_price: 64444,
          total: 4,
        },
        {
          delivery_time: "14.06.2022",
          order_num: 121123,
          dollar_price: 23,
          ruble_price: 1250,
          general_price: 44444,
          total: 14,
        }
      ],
    };
  }
  client = new W3CWebSocket('ws://127.0.0.1:8000/ws/orders/list/')
  componentDidMount() {
    var  self  =  this;
    this.client.onopen = () => {
      console.log('websucket')
    }
    this.client.onmessage = (gs_data) => {
      const dataFromSever = JSON.parse(gs_data.data);
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
        <XAxis dataKey="delivery_time" />
        <YAxis />
        <Tooltip />
        <Legend />
        <Line
          type="monotone"
          dataKey="general_price"
          stroke="#8884d8"
          activeDot={{ r: 2 }}
        />
        <Line type="monotone" dataKey="total" stroke="#82ca9d" />
      </LineChart>
    );
  }
}

export default OrdersChart;