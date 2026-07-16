from fastapi import APIRouter
from datetime import datetime

from app.database.database import SessionLocal
from app.models.models import WorkOrder

router = APIRouter()

@router.get("/tickets-at-risk")
def tickets_at_risk():

    db = SessionLocal()

    tickets = db.query(WorkOrder).all()

    result = []

    critical_count = 0
    high_count = 0
    medium_count = 0

    for ticket in tickets:

        if ticket.status == "Completed":
            continue

        # Determine severity
        if ticket.priority == "Critical":
            severity = "HIGH"
            critical_count += 1

        elif ticket.priority == "High":
            severity = "MEDIUM"
            high_count += 1

        else:
            severity = "LOW"
            medium_count += 1

        result.append({
            "work_order_id": ticket.work_order_id,
            "customer_name": ticket.customer_name,
            "location": ticket.location,
            "issue_type": ticket.issue_type,
            "priority": ticket.priority,
            "status": ticket.status,
            "assigned_technician": ticket.assigned_technician,
            "due_date": ticket.due_date,
            "severity": severity
        })

    return {
        "critical_tickets": critical_count,
        "high_priority_tickets": high_count,
        "other_tickets": medium_count,
        "tickets": result
    }