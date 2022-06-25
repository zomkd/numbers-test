// import "./index.css";
// import React from "react";
// import {
//   LineChart,
//   Line,
//   XAxis,
//   YAxis,
//   CartesianGrid,
//   Tooltip,
//   Legend
// } from "recharts";

// const data = [
//   {
//     name: "Page A",
//     uv: 4000,
//     pv: 2400,
//     amt: 2400
//   },
//   {
//     name: "Page B",
//     uv: 3000,
//     pv: 1398,
//     amt: 2210
//   },
//   {
//     name: "Page C",
//     uv: 2000,
//     pv: 9800,
//     amt: 2290
//   },
//   {
//     name: "Page D",
//     uv: 2780,
//     pv: 3908,
//     amt: 2000
//   },
//   {
//     name: "Page E",
//     uv: 1890,
//     pv: 4800,
//     amt: 2181
//   },
//   {
//     name: "Page F",
//     uv: 2390,
//     pv: 3800,
//     amt: 2500
//   },
//   {
//     name: "Page G",
//     uv: 3490,
//     pv: 4300,
//     amt: 2100
//   }
// ];

// export default function App() {
//   return (
//     <LineChart
//       width={500}
//       height={300}
//       data={data}
//       margin={{
//         top: 5,
//         right: 30,
//         left: 20,
//         bottom: 5
//       }}
//     >
//       <CartesianGrid strokeDasharray="3 3" />
//       <XAxis dataKey="name" />
//       <YAxis />
//       <Tooltip />
//       <Legend />
//       <Line
//         type="monotone"
//         dataKey="pv"
//         stroke="#8884d8"
//         activeDot={{ r: 8 }}
//       />
//       <Line type="monotone" dataKey="uv" stroke="#82ca9d" />
//     </LineChart>
//   );
// }
import  React, { Component } from  'react'; 
import  OrdersService  from  './OrdersService';
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
  // componentDidMount() {
  //   var  self  =  this;
  //   ordersService.getOrders().then(function (result) {
  //     console.log(result);
  //     self.setState({ orders:  result.data})
  //   });
  // }
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