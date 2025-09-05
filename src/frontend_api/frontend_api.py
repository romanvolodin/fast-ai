import asyncio
from datetime import datetime
from typing import Annotated

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, ConfigDict, EmailStr, Field
from pydantic.alias_generators import to_camel

from .mocks import mock_html

frontend_app = FastAPI(title="FrontendAPI")

UserName = Annotated[str, Field(min_length=3, max_length=100)]
SiteTitle = Annotated[str, Field(max_length=128)]


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


class CreateSiteRequest(BaseModel):
    title: SiteTitle | None = None
    prompt: str

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "title": "Фан клуб игры в домино",
                    "prompt": "Сайт любителей играть в домино",
                },
            ],
        },
    )


class SiteResponse(BaseModel):
    site_id: int
    title: SiteTitle | None
    prompt: str
    screenshot_url: str | None
    html_code_url: str | None
    html_code_download_url: str | None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        json_schema_extra={
            "examples": [
                {
                    "siteId": 1,
                    "title": "Фан клуб игры в домино",
                    "prompt": "Сайт любителей играть в домино",
                    "screenshotUrl": "http://example.com/media/index.png",
                    "html_code_url": "http://example.com/media/index.html",
                    "html_code_download_url": "http://example.com/media/index.html?response-content-disposition=attachment",
                    "createdAt": "2025-09-02T09:40:00+03:00",
                    "updatedAt": "2025-09-02T09:40:00+03:00",
                },
            ],
        },
    )


class Prompt(BaseModel):
    prompt: str

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "prompt": "Сайт любителей играть в хоккей",
                },
            ],
        },
    )


async def mock_generate_html():
    for line in mock_html.split("\n")[:50]:
        await asyncio.sleep(0.1)
        yield line


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


@frontend_app.post(
    "/sites/create",
    summary="Создать сайт",
    tags=["Sites"],
    response_model=SiteResponse,
)
def create_site(site: CreateSiteRequest) -> SiteResponse:
    return {
        "siteId": 100500,
        "title": "Фан клуб игры в домино",
        "prompt": "Сайт любителей играть в домино",
        "screenshotUrl": "http://example.com/media/index.png",
        "html_code_url": "http://example.com/media/index.html",
        "html_code_download_url": "http://example.com/media/index.html?response-content-disposition=attachment",
        "createdAt": "2025-09-02T09:40:00+03:00",
        "updatedAt": "2025-09-02T09:40:00+03:00",
    }


@frontend_app.post(
    "/sites/{site_id}/generate",
    summary="Сгенерировать HTML код сайта",
    tags=["Sites"],
)
def generate_site(site_id: int, prompt: Prompt | None = None) -> str:
    return StreamingResponse(
        content=mock_generate_html(),
        media_type="text/html; charset=utf-8",
    )


@frontend_app.get(
    "/sites/my",
    summary="Получить список сайтов для текущего пользователя",
    tags=["Sites"],
    response_model=list[SiteResponse],
)
def get_current_user_sites() -> list[SiteResponse]:
    return [
        {
            "siteId": 100500,
            "title": "Фан клуб игры в домино",
            "prompt": "Сайт любителей играть в домино",
            "screenshotUrl": "http://example.com/media/index.png",
            "html_code_url": "http://example.com/media/index.html",
            "html_code_download_url": "http://example.com/media/index.html?response-content-disposition=attachment",
            "createdAt": "2025-09-02T09:40:00+03:00",
            "updatedAt": "2025-09-02T09:40:00+03:00",
        },
        {
            "siteId": 100600,
            "title": "Фан клуб игры в хоккей",
            "prompt": "Сайт любителей играть в хоккей",
            "screenshotUrl": "http://example.com/media/index.png",
            "html_code_url": "http://example.com/media/index.html",
            "html_code_download_url": "http://example.com/media/index.html?response-content-disposition=attachment",
            "createdAt": "2025-09-02T09:40:00+03:00",
            "updatedAt": "2025-09-02T09:40:00+03:00",
        },
    ]


@frontend_app.get(
    "/sites/{site_id}",
    summary="Получить сайт по id",
    tags=["Sites"],
    response_model=SiteResponse,
)
def get_site_by_id(site_id: int) -> SiteResponse:
    return {
        "siteId": 100500,
        "title": "Фан клуб игры в домино",
        "prompt": "Сайт любителей играть в домино",
        "screenshotUrl": "http://example.com/media/index.png",
        "html_code_url": "http://example.com/media/index.html",
        "html_code_download_url": "http://example.com/media/index.html?response-content-disposition=attachment",
        "createdAt": "2025-09-02T09:40:00+03:00",
        "updatedAt": "2025-09-02T09:40:00+03:00",
    }
