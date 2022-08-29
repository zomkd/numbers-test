import React from "react";
import styles from "./TableRow.module.css";

export default function TableRow({ data }){
    return (
        <tr data-testid="table-row" className={styles.tableRowItems}>
            {Object.entries(data).map(([key,value]) => (
                <td className={styles.tableCell} key={key}>{value}</td>
            ))}
        </tr>
    );
};