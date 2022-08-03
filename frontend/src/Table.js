import React from "react";
import TableRow from "./TableRow";
import TableHeadItem from "./TableHeadItem";


export default function Table({theadData, tbodyData }){
    return (
        <table>
            <thead>
                <tr>
                    {theadData.map((h) => {
                        return <TableHeadItem key={h} item={h} />;
                    })}
                </tr>
            </thead>
            <tbody>
                {tbodyData.map((item) => {
                    return <TableRow key={item} data={item} />;
                })}
            </tbody>
        </table>
    );
}