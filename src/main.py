from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from frontend_api.frontend_api import frontend_app

app = FastAPI()
app.mount("/frontend-api", frontend_app)
app.mount("/", StaticFiles(directory="static", html=True), name="static")
