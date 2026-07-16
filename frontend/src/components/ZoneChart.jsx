import { useEffect, useState } from "react";
import { getZoneSummary } from "../services/api";

import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid
} from "recharts";

export default function ZoneChart() {

  const [zones, setZones] = useState([]);

  useEffect(() => {

    const fetchZones = async () => {

      try {

        const response = await getZoneSummary();

        setZones(response.data);

      } catch (error) {

        console.error(error);

      }

    };

    fetchZones();

  }, []);

  return (

    <div className="bg-white rounded-xl shadow-md p-5 mb-6">

      <h2 className="text-2xl font-bold mb-4">
        Zone Summary
      </h2>

      <ResponsiveContainer
        width="100%"
        height={350}
      >

        <BarChart data={zones}>

          <CartesianGrid strokeDasharray="3 3" />

          <XAxis dataKey="zone" />

          <YAxis />

          <Tooltip />

          <Bar
            dataKey="open_tickets"
          />

        </BarChart>

      </ResponsiveContainer>

    </div>

  );

}