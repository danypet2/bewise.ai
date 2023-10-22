from fastapi import FastAPI
from questions.routers import router as router_questions

app = FastAPI(
    title='BewiseTest'
)

app.include_router(router_questions)
