from dataclasses import dataclass
from unicodedata import category
from src.domain.entities import Article
from typing import List, Optional

from src.infrastructure.data.repository import ArticlesRepository

@dataclass
class GetArticleRequest:
    slug: str


class GetArticlesHandler:
    def __init__(self, articles_repository: ArticlesRepository):
        self.articles_repository = articles_repository

    def handle(self, request: GetArticleRequest) -> Article:
        article = self.articles_repository.find_by_slug(request.slug)
        parse_body = []
        for article_item in article.items:
            parse_body.append(article_item.item)
        article.body = parse_body
        return article

