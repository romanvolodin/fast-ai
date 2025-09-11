from fastapi import FastAPI

from .sites.router import router as sites_router
from .users.router import router as users_router

frontend_app = FastAPI(title="FrontendAPI")
frontend_app.include_router(users_router)
frontend_app.include_router(sites_router)
