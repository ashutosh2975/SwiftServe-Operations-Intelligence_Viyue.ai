from fastapi import APIRouter
from app.database.database import SessionLocal
from app.models.models import WorkOrder, Equipment, SLAMetric

router = APIRouter()

@router.get("/alerts")
def get_alerts():

    db = SessionLocal()

    alerts = []

    # Critical Equipment
    equipment = db.query(Equipment).all()

    for item in equipment:
        if item.critical_alerts > 2:
            alerts.append({
                "type": "CRITICAL_EQUIPMENT",
                "equipment": item.equipment_name,
                "message": f"{item.equipment_name} has {item.critical_alerts} critical alerts"
            })

    # SLA Breaches
    customers = db.query(SLAMetric).all()

    for customer in customers:
        if customer.sla_compliance_percent < 95:
            alerts.append({
                "type": "SLA_RISK",
                "customer": customer.customer_name,
                "message": f"SLA compliance dropped to {customer.sla_compliance_percent}%"
            })

    return alerts