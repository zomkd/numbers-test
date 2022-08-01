import React from "react";
import { Card, CardTitle, CardBody, CardText } from "reactstrap";
import { QueryRenderer } from "@cubejs-client/react";

const Chart = ({ title, query, render }) => (
  <Card>
    <CardBody>
      <CardTitle tag="h5">{title}</CardTitle>
      <CardText>
        <QueryRenderer
          query={query}
          render={({ resultSet }) => {
            if (!resultSet) {
              return <div className="loader" />;
            }

            return render(resultSet);
          }}
        />
      </CardText>
    </CardBody>
  </Card>
);

export default Chart;
