import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

// KPI
export const getKPIs = () => API.get("/kpis");

// Alerts
export const getAlerts = () => API.get("/alerts");

// Work Orders
export const getWorkOrders = () => API.get("/work-orders");
export const getOpenWorkOrders = () => API.get("/work-orders/open");

// Zone Summary
export const getZoneSummary = () => API.get("/zone-summary");

// AI Brief
export const getMorningBrief = () => API.get("/morning-brief");

// SLA
export const getSLABreaches = () => API.get("/sla-breaches");

// Risk Tickets
export const getTicketsAtRisk = () => API.get("/tickets-at-risk");