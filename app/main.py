from fastapi import FastAPI

from app.routers import health, math

app = FastAPI()

app.include_router(health.router)
app.include_router(math.router)
