
from email.policy import default
from src.domain.entities import Article, ArticleItem, Item
from sqlalchemy import Table, MetaData, Column, String, DateTime, Boolean, Text, ForeignKey, UniqueConstraint, Integer
from sqlalchemy.orm import mapper, relationship
from sqlalchemy.sql import func


metadata = MetaData()

articles = Table(
    "articles",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("title", String(255)),
    Column("slug", String(255), index=True),
    Column("published", Boolean, default=False, index=True),
    Column("date_created", DateTime(timezone=True), server_default=func.now()),
    Column("date_modified", DateTime(timezone=True), onupdate=func.now()),
    Column("category", String(255)),
    Column("image", String(255)),
    UniqueConstraint('slug', name='uix_0'),
)

items = Table(
    "items",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("type", String(255), index=True),
    Column("title", String(255)),
    Column("content", Text),
    Column("date_created", DateTime(timezone=True), server_default=func.now()),
    Column("date_modified", DateTime(timezone=True), onupdate=func.now()),
)

article_items = Table(
    "article_items",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("article_id", Integer, ForeignKey('articles.id')),
    Column("item_id", Integer, ForeignKey('items.id')),
    Column("order", Integer, default=1),
    Column("date_created", DateTime(timezone=True), server_default=func.now()),
    Column("date_modified", DateTime(timezone=True), onupdate=func.now()),
    UniqueConstraint('article_id', 'item_id', name='uix_1')
)

def start_mappers():
    mapper(ArticleItem, article_items)
    mapper(Item, items, properties={
        'articles': relationship(ArticleItem, backref='item')
    })
    mapper(Article, articles, properties={
        'items': relationship(ArticleItem, backref='article')
    })