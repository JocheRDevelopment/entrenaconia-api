import logging
from fastapi import APIRouter, Body
from pydantic import BaseModel
from app.services.training_plan_service import generate_plan
from app.models.schemas import TrainingPlanRequest

router = APIRouter()

logger = logging.getLogger(__name__)


@router.post("/generate-plan/")
def generate_training_plan(training_plan: TrainingPlanRequest):
    logger.info(training_plan)
    plan = generate_plan(training_plan.user_id, training_plan.distance)
    return {"plan": plan}