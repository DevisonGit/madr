from fastapi import FastAPI

from src.madr.users.routes import router as users_router

app = FastAPI()

app.include_router(users_router)


@app.get('/')
def read_root():
    return {'message': 'MADR'}
