from fastapi.routing import APIRouter

from .schemas import UserDetailsResponse

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
    response_model=UserDetailsResponse,
)
def get_current_user() -> UserDetailsResponse:
    return {
        "profileId": 1,
        "email": "user@fast.ai",
        "username": "FastUser",
        "registeredAt": "2025-09-02T09:40:00+03:00",
        "updatedAt": "2025-09-02T09:40:00+03:00",
        "isActive": True,
    }
