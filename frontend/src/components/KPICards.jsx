import { useEffect, useState } from "react";
import { getKPIs } from "../services/api";

export default function KPICards() {
  const [kpis, setKpis] = useState(null);

  useEffect(() => {
    const fetchKPIs = async () => {
      try {
        const response = await getKPIs();

        console.log("API Response:", response.data);

        setKpis(response.data);
      } catch (error) {
        console.error("Error fetching KPIs:", error);
      }
    };

    fetchKPIs();
  }, []);

  if (!kpis) {
    return (
      <div className="text-center text-lg font-semibold">
        Loading KPI Data...
      </div>
    );
  }

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-5 mb-6">

      <div className="bg-white rounded-xl shadow-md p-5">
        <h3 className="text-gray-500">Open Work Orders</h3>
        <p className="text-3xl font-bold">
          {kpis.open_work_orders}
        </p>
      </div>

      <div className="bg-white rounded-xl shadow-md p-5">
        <h3 className="text-gray-500">SLA Compliance</h3>
        <p className="text-3xl font-bold">
          {kpis.avg_sla_compliance}%
        </p>
      </div>

      <div className="bg-white rounded-xl shadow-md p-5">
        <h3 className="text-gray-500">Critical Equipment</h3>
        <p className="text-3xl font-bold">
          {kpis.critical_equipment}
        </p>
      </div>

      <div className="bg-white rounded-xl shadow-md p-5">
        <h3 className="text-gray-500">Technicians</h3>
        <p className="text-3xl font-bold">
          {kpis.total_technicians}
        </p>
      </div>

    </div>
  );
}