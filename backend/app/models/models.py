from sqlalchemy import Column, Integer, String, Float
from app.database.database import Base

class Technician(Base):
    __tablename__ = "technicians"

    id = Column(Integer, primary_key=True)
    technician_id = Column(String)
    name = Column(String)
    location = Column(String)
    status = Column(String)
    skills = Column(String)
    total_assignments = Column(Integer)
    completed_assignments = Column(Integer)
    avg_response_time_hours = Column(Float)


class WorkOrder(Base):
    __tablename__ = "work_orders"

    id = Column(Integer, primary_key=True)

    work_order_id = Column(String)
    customer_name = Column(String)
    location = Column(String)
    issue_type = Column(String)
    priority = Column(String)
    status = Column(String)

    assigned_technician = Column(String)

    created_date = Column(String)
    due_date = Column(String)
    completed_date = Column(String)

    resolution_time_hours = Column(Float)
    estimated_cost_inr = Column(Float)
    

class Equipment(Base):
    __tablename__ = "equipment"

    id = Column(Integer, primary_key=True)
    equipment_id = Column(String)
    equipment_name = Column(String)
    status = Column(String)
    critical_alerts = Column(Integer)


class SLAMetric(Base):
    __tablename__ = "sla_metrics"

    id = Column(Integer, primary_key=True)
    customer_name = Column(String)
    sla_compliance_percent = Column(Float)
    sla_breaches_this_month = Column(Integer)


class DispatchLog(Base):
    __tablename__ = "dispatch_logs"

    id = Column(Integer, primary_key=True)
    dispatch_id = Column(String)
    work_order_id = Column(String)
    technician_id = Column(String)
    status = Column(String)