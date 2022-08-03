import React from "react";

export default function TableRow({ data }){
    return (
        <tr>
            {Object.entries(data).map(([key,value]) => (
                <td key={key}>{value}</td>
            ))}
        </tr>
    );
};