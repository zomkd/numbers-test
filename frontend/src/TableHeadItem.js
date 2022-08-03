import React from "react";

export default function TableHeadItem({ item }){
    return (
        <td title={item}>
            {item}
        </td>
    );
};