from datetime import datetime
from typing import Annotated

from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict, EmailStr, Field
from pydantic.alias_generators import to_camel

frontend_app = FastAPI(title="FrontendAPI")

UserName = Annotated[str, Field(min_length=3, max_length=100)]


class UserResponse(BaseModel):
    profile_id: int
    email: EmailStr
    username: UserName
    registered_at: datetime
    updated_at: datetime
    is_active: bool

    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        json_schema_extra={
            "examples": [
                {
                    "profileId": 1,
                    "email": "user@example.com",
                    "username": "User Name",
                    "registeredAt": "2025-09-02T09:40:00+03:00",
                    "updatedAt": "2025-09-02T09:40:00+03:00",
                    "isActive": True,
                },
            ],
        },
    )


@frontend_app.get(
    "/users/me",
    summary="Получить учетные данные текущего пользователя",
    response_description="Данные пользователя",
    tags=["Users"],
    response_model=UserResponse,
)
def get_current_user() -> UserResponse:
    return {
        "profileId": 1,
        "email": "user@fast.ai",
        "username": "FastUser",
        "registeredAt": "2025-09-02T09:40:00+03:00",
        "updatedAt": "2025-09-02T09:40:00+03:00",
        "isActive": True,
    }
