import KPICards from "../components/KPICards";
import AlertsPanel from "../components/AlertsPanel";
import TicketsAtRisk from "../components/TicketsAtRisk";
import ZoneChart from "../components/ZoneChart";
import WorkOrdersTable from "../components/WorkOrdersTable";
import MorningBrief from "../components/MorningBrief";

export default function Dashboard() {
  return (
    <div className="min-h-screen bg-gray-100 p-8">

      {/* Header */}
      <div className="mb-8">

        <h1 className="text-5xl font-bold text-gray-800">
          SwiftServe Operations Intelligence
        </h1>

        <p className="text-gray-600 mt-2 text-lg">
          Real-Time Operations Control Tower
        </p>

      </div>

      {/* KPI Cards */}
      <KPICards />

      {/* Quick Status Cards */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">

        <div className="bg-green-100 p-4 rounded-xl shadow">
          <h3 className="font-semibold text-green-800">
            SLA Status
          </h3>
          <p className="text-xl font-bold">
            Healthy
          </p>
        </div>

        <div className="bg-yellow-100 p-4 rounded-xl shadow">
          <h3 className="font-semibold text-yellow-800">
            Attention Required
          </h3>
          <p className="text-xl font-bold">
            Tickets At Risk
          </p>
        </div>

        <div className="bg-red-100 p-4 rounded-xl shadow">
          <h3 className="font-semibold text-red-800">
            Active Alerts
          </h3>
          <p className="text-xl font-bold">
            Critical Issues
          </p>
        </div>

      </div>

      {/* Alerts */}
      <AlertsPanel />

      {/* Tickets At Risk */}
      <TicketsAtRisk />

      {/* Zone Summary */}
      <ZoneChart />

      {/* Work Orders */}
      <WorkOrdersTable />

      {/* AI Morning Brief */}
      <MorningBrief />

        <div className="text-center text-gray-500 mt-10 mb-5">
            SwiftServe Operations Intelligence Dashboard | React + FastAPI + SQLite + Groq AI
        </div>
    </div>
    
  );
}