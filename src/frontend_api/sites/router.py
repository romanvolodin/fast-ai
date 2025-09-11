from fastapi.responses import StreamingResponse
from fastapi.routing import APIRouter

from .mocks import mock_generate_html
from .schemas import (
    CreateSiteRequest,
    GeneratedSitesResponse,
    SiteGenerationRequest,
    SiteResponse,
)

router = APIRouter(
    prefix="/sites",
    tags=[
        "Sites",
    ],
)


@router.get(
    "/my",
    summary="Получить список сайтов для текущего пользователя",
    response_model=GeneratedSitesResponse,
)
def get_current_user_sites() -> GeneratedSitesResponse:
    return {
        "sites": [
            {
                "id": 100500,
                "title": "Фан клуб игры в домино",
                "prompt": "Сайт любителей играть в домино",
                "screenshotUrl": "http://example.com/media/index.png",
                "html_code_url": "http://example.com/media/index.html",
                "html_code_download_url": "http://example.com/media/index.html?response-content-disposition=attachment",
                "createdAt": "2025-09-02T09:40:00+03:00",
                "updatedAt": "2025-09-02T09:40:00+03:00",
            },
            {
                "id": 100600,
                "title": "Фан клуб игры в хоккей",
                "prompt": "Сайт любителей играть в хоккей",
                "screenshotUrl": "http://example.com/media/index.png",
                "html_code_url": "http://example.com/media/index.html",
                "html_code_download_url": "http://example.com/media/index.html?response-content-disposition=attachment",
                "createdAt": "2025-09-02T09:40:00+03:00",
                "updatedAt": "2025-09-02T09:40:00+03:00",
            },
        ],
    }


@router.post(
    "/create",
    summary="Создать сайт",
    response_model=SiteResponse,
)
def create_site(site: CreateSiteRequest) -> SiteResponse:
    return {
        "id": 100500,
        "title": "Фан клуб игры в домино",
        "prompt": "Сайт любителей играть в домино",
        "screenshotUrl": "http://example.com/media/index.png",
        "html_code_url": "http://example.com/media/index.html",
        "html_code_download_url": "http://example.com/media/index.html?response-content-disposition=attachment",
        "createdAt": "2025-09-02T09:40:00+03:00",
        "updatedAt": "2025-09-02T09:40:00+03:00",
    }


@router.post(
    "/{site_id}/generate",
    summary="Сгенерировать HTML код сайта",
)
def generate_site(site_id: int, prompt: SiteGenerationRequest | None = None) -> str:
    return StreamingResponse(
        content=mock_generate_html(),
        media_type="text/html; charset=utf-8",
    )


@router.get(
    "/{site_id}",
    summary="Получить сайт по id",
    response_model=SiteResponse,
)
def get_site_by_id(site_id: int) -> SiteResponse:
    return {
        "id": 100500,
        "title": "Фан клуб игры в домино",
        "prompt": "Сайт любителей играть в домино",
        "screenshotUrl": "http://example.com/media/index.png",
        "html_code_url": "http://example.com/media/index.html",
        "html_code_download_url": "http://example.com/media/index.html?response-content-disposition=attachment",
        "createdAt": "2025-09-02T09:40:00+03:00",
        "updatedAt": "2025-09-02T09:40:00+03:00",
    }
