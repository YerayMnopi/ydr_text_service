from dataclasses import dataclass
from unicodedata import category
from src.domain.entities import Article
from typing import List, Optional

from src.infrastructure.data.repository import ArticlesRepository

@dataclass
class GetArticlesRequest:
    category: Optional[str]


class GetArticlessHandler:
    def __init__(self, articles_repository: ArticlesRepository):
        self.articles_repository = articles_repository

    def handle(self, request: GetArticlesRequest) -> List[Article]:
        return self.articles_repository.list(request.category)

