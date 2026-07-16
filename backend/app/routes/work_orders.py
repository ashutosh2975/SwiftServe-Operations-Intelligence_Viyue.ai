from fastapi import APIRouter
from app.database.database import SessionLocal
from app.models.models import WorkOrder

router = APIRouter()


@router.get("/work-orders")
def get_work_orders():

    db = SessionLocal()

    work_orders = db.query(WorkOrder).all()

    return [
        {
            "work_order_id": wo.work_order_id,
            "customer_name": wo.customer_name,
            "location": wo.location,
            "issue_type": wo.issue_type,
            "priority": wo.priority,
            "status": wo.status,
            "assigned_technician": wo.assigned_technician,
            "due_date": wo.due_date
        }
        for wo in work_orders
    ]


@router.get("/work-orders/open")
def get_open_work_orders():

    db = SessionLocal()

    open_orders = db.query(WorkOrder).filter(
        WorkOrder.status != "Completed"
    ).all()

    return [
        {
            "work_order_id": wo.work_order_id,
            "customer_name": wo.customer_name,
            "priority": wo.priority,
            "status": wo.status,
            "assigned_technician": wo.assigned_technician
        }
        for wo in open_orders
    ]