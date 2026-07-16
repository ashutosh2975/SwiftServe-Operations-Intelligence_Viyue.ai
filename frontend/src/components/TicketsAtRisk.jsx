import { useEffect, useState } from "react";
import { getTicketsAtRisk } from "../services/api";

export default function TicketsAtRisk() {

  const [data, setData] = useState(null);

  useEffect(() => {

    const fetchTickets = async () => {

      try {
        const response = await getTicketsAtRisk();
        setData(response.data);
      }
      catch (error) {
        console.error(error);
      }

    };

    fetchTickets();

  }, []);

  if (!data) {
    return (
      <div className="bg-white rounded-xl shadow-md p-5 mb-6">
        Loading Tickets...
      </div>
    );
  }

  return (
    <div className="bg-white rounded-xl shadow-md p-5 mb-6">

      <h2 className="text-2xl font-bold mb-4">
        Tickets At Risk
      </h2>

      {/* Summary Cards */}

      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">

        <div className="bg-red-100 p-4 rounded">
          <p className="text-sm">Critical</p>
          <h3 className="text-2xl font-bold">
            {data.critical_tickets}
          </h3>
        </div>

        <div className="bg-yellow-100 p-4 rounded">
          <p className="text-sm">High Priority</p>
          <h3 className="text-2xl font-bold">
            {data.high_priority_tickets}
          </h3>
        </div>

        <div className="bg-blue-100 p-4 rounded">
          <p className="text-sm">Other</p>
          <h3 className="text-2xl font-bold">
            {data.other_tickets}
          </h3>
        </div>

      </div>

      {/* Table */}

      <table className="w-full border">

        <thead>

          <tr className="bg-gray-200">
            <th className="p-2">Work Order</th>
            <th className="p-2">Customer</th>
            <th className="p-2">Priority</th>
            <th className="p-2">Status</th>
            <th className="p-2">Severity</th>
          </tr>

        </thead>

        <tbody>

          {data.tickets.map((ticket) => (

            <tr
              key={ticket.work_order_id}
              className="border-t"
            >

              <td className="p-2">
                {ticket.work_order_id}
              </td>

              <td className="p-2">
                {ticket.customer_name}
              </td>

              <td className="p-2">
                {ticket.priority}
              </td>

              <td className="p-2">
                {ticket.status}
              </td>

              <td className="p-2">

                <span
                  className={
                    ticket.severity === "HIGH"
                      ? "bg-red-500 text-white px-2 py-1 rounded"
                      : "bg-yellow-500 text-white px-2 py-1 rounded"
                  }
                >

                  {ticket.severity}

                </span>

              </td>

            </tr>

          ))}

        </tbody>

      </table>

    </div>
  );
}