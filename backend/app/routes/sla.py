from fastapi import APIRouter
from datetime import datetime

from app.database.database import SessionLocal
from app.models.models import WorkOrder

router = APIRouter()

@router.get("/sla-breaches")
def sla_breaches():

    db = SessionLocal()

    orders = db.query(WorkOrder).all()

    breached = []

    for order in orders:

        try:

            due_date = datetime.strptime(
                order.due_date,
                "%Y-%m-%d"
            )

            if (
                order.status != "Completed"
            ):

                breached.append({
                    "work_order_id": order.work_order_id,
                    "customer": order.customer_name,
                    "priority": order.priority,
                    "status": order.status,
                    "due_date": order.due_date,
                    "severity": "HIGH"
                    if order.priority == "Critical"
                    else "MEDIUM"
                })

        except:
            pass

    return breached