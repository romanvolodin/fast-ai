from fastapi import FastAPI

frontend_app = FastAPI(title="FrontendAPI")


@frontend_app.get("/users/me")
def get_current_user():
    return {
        "profileId": 1,
        "email": "user@fast.ai",
        "username": "FastUser",
        "registeredAt": "2025-09-02T09:40:00+03:00",
        "updatedAt": "2025-09-02T09:40:00+03:00",
        "isActive": True,
    }
