from fastapi import APIRouter
from app.database.database import SessionLocal
from app.models.models import WorkOrder, Equipment, SLAMetric
from app.services.ai_service import generate_morning_brief

router = APIRouter()

@router.get("/morning-brief")
def morning_brief():

    db = SessionLocal()

    open_orders = db.query(WorkOrder).filter(
        WorkOrder.status != "Completed"
    ).count()

    critical_equipment = db.query(Equipment).filter(
        Equipment.critical_alerts > 2
    ).count()

    risky_customers = db.query(SLAMetric).filter(
        SLAMetric.sla_compliance_percent < 95
    ).count()

    data = {
        "open_orders": open_orders,
        "critical_equipment": critical_equipment,
        "risky_customers": risky_customers
    }

    brief = generate_morning_brief(data)

    return {
        "brief": brief
    }