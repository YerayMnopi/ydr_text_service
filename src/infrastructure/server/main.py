from typing import Any, Optional
from src.application.get_article import GetArticleRequest, GetArticlesHandler
from src.application.get_articles_list import GetArticlesRequest, GetArticlessHandler
from src.infrastructure.data.repository import ArticlesRepository
from src.settings import get_settings
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..data.mappers import start_mappers
from fastapi.middleware.cors import CORSMiddleware

start_mappers()
get_session = sessionmaker(bind=create_engine(get_settings().get_postgres_uri()))


app: Any = FastAPI()
origins = [
    "http://localhost:4200",
    "http://localhost:4000",
    "https://softay.es",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/articles/")
async def root(category: str | None = None):
    articles_repo = ArticlesRepository(get_session())
    request = GetArticlesRequest(category=category)
    articles = GetArticlessHandler(articles_repo).handle(request)

    return articles


@app.get("/articles/{slug}")
async def root(slug: str):
    articles_repo = ArticlesRepository(get_session())
    request = GetArticleRequest(slug=slug)
    article = GetArticlesHandler(articles_repo).handle(request)
    del(article.items)
    return article


