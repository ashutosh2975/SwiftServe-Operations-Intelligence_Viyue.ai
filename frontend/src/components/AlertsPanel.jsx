import { useEffect, useState } from "react";
import { getAlerts } from "../services/api";

export default function AlertsPanel() {

  const [alerts, setAlerts] = useState([]);

  useEffect(() => {

    const fetchAlerts = async () => {

      try {
        const response = await getAlerts();
        setAlerts(response.data);
      }
      catch (error) {
        console.error(error);
      }

    };

    fetchAlerts();

  }, []);

  return (
    <div className="bg-white rounded-xl shadow-md p-5 mb-6">

      <h2 className="text-2xl font-bold mb-4">
        Critical Alerts
      </h2>

      {
        alerts.length === 0
          ? <p>No active alerts</p>
          : alerts.map((alert, index) => (

            <div
              key={index}
              className="bg-red-100 border-l-4 border-red-500 p-3 mb-3 rounded"
            >

              <p className="font-semibold">
                {alert.type}
              </p>

              <p>
                {alert.message}
              </p>

            </div>

          ))
      }

    </div>
  );
}