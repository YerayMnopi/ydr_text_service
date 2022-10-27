import abc
from typing import List
from src.domain.entities import Article, ArticleItem


class AbstractArticlesRepository(abc.ABC):
    def __init__(self, session):
        self.session = session

    @abc.abstractmethod
    def list(self) -> List[Article]:
        raise NotImplementedError

    @abc.abstractmethod
    def find_by_slug(self, slug: str) -> Article:
        raise NotImplementedError


class ArticlesRepository(AbstractArticlesRepository):
    def __init__(self, session):
        self.session = session

    def list(self, category=None) -> List[Article]:
        if category:
            return self.session.query(Article).filter_by(category=category).all()
        return self.session.query(Article).all()

    def find_by_slug(self, slug: str) -> Article:
        return self.session.query(Article).filter_by(slug=slug).first()

