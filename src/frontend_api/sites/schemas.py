from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel

SiteTitle = Annotated[str, Field(max_length=128)]


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
    id: int
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


class GeneratedSitesResponse(BaseModel):
    sites: list[SiteResponse]

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "sites": [
                        {
                            "id": 1,
                            "title": "Фан клуб игры в регби",
                            "prompt": "Сайт любителей играть в регби",
                            "screenshotUrl": "http://example.com/media/index.png",
                            "html_code_url": "http://example.com/media/index.html",
                            "html_code_download_url": "http://example.com/media/index.html?response-content-disposition=attachment",
                            "createdAt": "2025-09-02T09:40:00+03:00",
                            "updatedAt": "2025-09-02T09:40:00+03:00",
                        },
                        {
                            "id": 2,
                            "title": "Фан клуб игры в теннис",
                            "prompt": "Сайт любителей играть в теннис",
                            "screenshotUrl": "http://example.com/media/index.png",
                            "html_code_url": "http://example.com/media/index.html",
                            "html_code_download_url": "http://example.com/media/index.html?response-content-disposition=attachment",
                            "createdAt": "2025-09-02T09:40:00+03:00",
                            "updatedAt": "2025-09-02T09:40:00+03:00",
                        },
                    ],
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
