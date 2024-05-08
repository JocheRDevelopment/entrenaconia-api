from fastapi import FastAPI
from app.routes import training_plan

app = FastAPI()

app.include_router(training_plan.router)
