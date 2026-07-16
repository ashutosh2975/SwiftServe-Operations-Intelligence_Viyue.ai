from app.database.database import engine
from app.models.models import *

Base.metadata.create_all(bind=engine)

print("Database Created")
