import { React } from "react";
import { Card, CardTitle, CardBody, CardText } from "reactstrap";


const Chart = ({ orders }) => {
  let total = 0;
  for (let i = 0; i < orders.length; ++i) {
    total += orders[i]['стоимость,$']
  }
  return (<Card
    className="my-2"
    color="primary"
    style={{
      width: '18rem'
    }}>
    <CardBody>
      <CardTitle tag="h5"> Total </CardTitle>
      <CardText>
        {total}
      </CardText>
    </CardBody>
  </Card>);
};

export default Chart
