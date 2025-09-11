from fastapi.routing import APIRouter

from .schemas import UserResponse

router = APIRouter(
    prefix="/users",
    tags=[
        "Users",
    ],
)


@router.get(
    "/me",
    summary="Получить учетные данные текущего пользователя",
    response_description="Данные пользователя",
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
