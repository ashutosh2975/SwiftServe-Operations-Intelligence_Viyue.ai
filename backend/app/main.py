from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.dashboard import router as dashboard_router
from app.routes.alerts import router as alerts_router
from app.routes.work_orders import router as work_orders_router
from app.routes.zones import router as zone_router
from app.routes.brief import router as brief_router
from app.routes.sla import router as sla_router
from app.routes.tickets import router as tickets_router

app = FastAPI(
    title="SwiftServe Operations Intelligence"
)

# -------------------------
# CORS
# -------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# Routes
# -------------------------

app.include_router(dashboard_router)
app.include_router(alerts_router)
app.include_router(work_orders_router)
app.include_router(zone_router)
app.include_router(brief_router)
app.include_router(sla_router)
app.include_router(tickets_router)