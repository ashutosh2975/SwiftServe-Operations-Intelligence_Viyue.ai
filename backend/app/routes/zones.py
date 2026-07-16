from fastapi import APIRouter
from app.database.database import SessionLocal
from app.models.models import WorkOrder, Technician

router = APIRouter()

@router.get("/zone-summary")
def zone_summary():

    db = SessionLocal()

    zones = ["Mumbai", "Pune", "Bangalore"]

    result = []

    for zone in zones:

        open_tickets = db.query(WorkOrder).filter(
            WorkOrder.location == zone,
            WorkOrder.status != "Completed"
        ).count()

        critical_tickets = db.query(WorkOrder).filter(
            WorkOrder.location == zone,
            WorkOrder.priority == "Critical",
            WorkOrder.status != "Completed"
        ).count()

        available_techs = db.query(Technician).filter(
            Technician.location == zone,
            Technician.status == "Active"
        ).count()

        result.append({
            "zone": zone,
            "open_tickets": open_tickets,
            "critical_tickets": critical_tickets,
            "available_technicians": available_techs
        })

    return result