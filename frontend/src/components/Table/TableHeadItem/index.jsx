import React from "react";
import styles from "./TableHeadItem.module.css";

export default function TableHeadItem({ item }){
    return (
        <td data-testid="table-head-item" className={styles.tableHeader} title={item}>
            {item}
        </td>
    );
};