import React from "react";
import styles from "./TableHeadItem.module.css";

export default function TableHeadItem({ item }){
    return (
        <td data-testid="head-item-table" className={styles.tableHeader} title={item}>
            {item}
        </td>
    );
};