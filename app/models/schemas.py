# models/schemas.py

from pydantic import BaseModel

class TrainingPlanRequest(BaseModel):
    user_id: str
    distance: str
