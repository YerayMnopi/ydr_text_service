from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List

class Category(Enum):
    BACKEND = 'Back-end engineering'
    FRONTEND = 'Front-end engineering'
    UX = 'User experience'
    AI = 'Artificial Intelligence'    


class ItemType(Enum):
    CONCEPT = 'Concept'
    PARAGRAPH = 'Paragraph'
    QUOTE = 'Quote'
    CODE = 'Code'
    IMAGE = 'Image'


class Item:
    id: int
    type: ItemType
    title: str
    content: str
    author: str
    reference: str    
    date_created: datetime
    date_modified: datetime
    
    def __repr__(self):
        return f'{self.type}: {self.title}'
    
class Article:
    id: int
    title: str
    slug: str
    published: bool = False
    date_created: datetime
    date_modified: datetime
    body: List[Item]
    category: Category
    image: str
    
    def __init__(self,
        id: int,
        title: str,
        slug: str,
        published: bool,
        date_created: datetime,
        body: List[Item],
        category: Category,
        image: str
    ):
        self.id = id
        self.title = title
        self.slug = slug
        self.published = published
        self.date_created = date_created
        self.body = body
        self.category = category
        self.image = image

    def __repr__(self):
        return self.title
    
    
class ArticleItem:
    id: int
    article_id: int
    item_id: int
    order: int

    def __repr__(self):
        return f'{self.article_id}: {self.order}'
    
    