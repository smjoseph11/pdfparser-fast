from decimal import Decimal
from sqlmodel import Field, SQLModel

class Document(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    document_name: str
    total_pages: int


class Page(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    page_number: int
    page_text: str


class BoundingBox(SQLModel, table=True):
        id: int | None = Field(default=None, primary_key=True)
        word_text: str
        x: Decimal
        y: Decimal
        width: Decimal
        height: Decimal
        page: 