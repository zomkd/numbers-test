import React, { useState } from "react";

import useTable from "../../hooks/useTable";
import styles from "./Table.module.css";
import TableFooter from "./TableFooter";
import TableHeadItem from "./TableHeadItem/TableHeadItem";
import TableRow from "./TableRow/TableRow";


const Table = ({ data, theadData, rowsPerPage }) => {
  const [page, setPage] = useState(1)
  const { slice, range } = useTable(data, page, rowsPerPage)

  return (
    <>    
    <table className={styles.table}>
      <thead className={styles.tableRowHeader}>
        <tr>
          {theadData.map((h) => {
            return <TableHeadItem key={h} item={h} />;
          })}
        </tr>
      </thead>
      <tbody>
        {slice.map((el) => {
          return <TableRow key={el} data={el} />;
        })}
      </tbody>
    </table>
    <TableFooter range={range} slice={slice} setPage={setPage} page={page} />
    </>

  )
};

export default Table;