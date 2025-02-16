from fastapi import FastAPI

from madr.routers import health

app = FastAPI()

app.include_router(health.router)
