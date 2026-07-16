from fastapi import APIRouter
from sqlalchemy import func

from app.database.database import SessionLocal
from app.models.models import *

router = APIRouter()

@router.get("/kpis")
def get_kpis():

    db = SessionLocal()

    open_work_orders = db.query(WorkOrder).filter(
        WorkOrder.status != "Completed"
    ).count()

    avg_sla = db.query(
        func.avg(SLAMetric.sla_compliance_percent)
    ).scalar()

    critical_equipment = db.query(
        Equipment
    ).filter(
        Equipment.critical_alerts > 2
    ).count()

    technicians = db.query(Technician).count()

    return {
        "open_work_orders": open_work_orders,
        "avg_sla_compliance": round(avg_sla, 2),
        "critical_equipment": critical_equipment,
        "total_technicians": technicians
    }