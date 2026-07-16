import { useEffect, useState } from "react";
import { getWorkOrders } from "../services/api";

export default function WorkOrdersTable() {

  const [orders, setOrders] = useState([]);

  useEffect(() => {

    const fetchOrders = async () => {

      try {

        const response = await getWorkOrders();

        setOrders(response.data);

      } catch (error) {

        console.error(error);

      }

    };

    fetchOrders();

  }, []);

  return (

    <div className="bg-white rounded-xl shadow-md p-5 mb-6">

      <h2 className="text-2xl font-bold mb-4">
        Work Orders
      </h2>

      <table className="w-full border">

        <thead>

          <tr className="bg-gray-200">

            <th className="p-2">ID</th>
            <th className="p-2">Customer</th>
            <th className="p-2">Priority</th>
            <th className="p-2">Status</th>

          </tr>

        </thead>

        <tbody>

          {orders.map((order) => (

            <tr
              key={order.work_order_id}
              className="border-t"
            >

              <td className="p-2">
                {order.work_order_id}
              </td>

              <td className="p-2">
                {order.customer_name}
              </td>

              <td className="p-2">
                {order.priority}
              </td>

              <td className="p-2">
                {order.status}
              </td>

            </tr>

          ))}

        </tbody>

      </table>

    </div>

  );

}