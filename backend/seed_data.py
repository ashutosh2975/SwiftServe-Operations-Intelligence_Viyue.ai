import pandas as pd

from app.database.database import SessionLocal
from app.models.models import *

db = SessionLocal()

# --------------------------
# TECHNICIANS
# --------------------------

tech_df = pd.read_csv("data/swiftserve_technicians.csv")

for _, row in tech_df.iterrows():

    technician = Technician(
        technician_id=row["technician_id"],
        name=row["name"],
        location=row["location"],
        status=row["status"],
        skills=row["skills"],
        total_assignments=row["total_assignments"],
        completed_assignments=row["completed_assignments"],
        avg_response_time_hours=row["avg_response_time_hours"]
    )

    db.add(technician)

# --------------------------
# WORK ORDERS
# --------------------------

wo_df = pd.read_csv("data/swiftserve_work_orders.csv")

for _, row in wo_df.iterrows():

    work_order = WorkOrder(
        work_order_id=row["work_order_id"],
        customer_name=row["customer_name"],
        location=row["location"],
        issue_type=row["issue_type"],
        priority=row["priority"],
        status=row["status"],
        assigned_technician=row["assigned_technician"],
        due_date=str(row["due_date"])
    )

    db.add(work_order)

# --------------------------
# EQUIPMENT
# --------------------------

equipment_df = pd.read_csv("data/swiftserve_equipment.csv")

for _, row in equipment_df.iterrows():

    equipment = Equipment(
        equipment_id=row["equipment_id"],
        equipment_name=row["equipment_name"],
        status=row["status"],
        critical_alerts=row["critical_alerts"]
    )

    db.add(equipment)

# --------------------------
# SLA
# --------------------------

sla_df = pd.read_csv("data/swiftserve_sla_metrics.csv")

for _, row in sla_df.iterrows():

    sla = SLAMetric(
        customer_name=row["customer_name"],
        sla_compliance_percent=row["sla_compliance_percent"],
        sla_breaches_this_month=row["sla_breaches_this_month"]
    )

    db.add(sla)

# --------------------------
# DISPATCH
# --------------------------

dispatch_df = pd.read_csv("data/swiftserve_dispatch_logs.csv")

for _, row in dispatch_df.iterrows():

    dispatch = DispatchLog(
        dispatch_id=row["dispatch_id"],
        work_order_id=row["work_order_id"],
        technician_id=row["technician_id"],
        status=row["status"]
    )

    db.add(dispatch)

db.commit()

print("Data Imported Successfully")