from sqlmodel import Field, Relationship, SQLModel


class Document(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    document_name: str
    total_pages: int
    pages: list["Page"] = Relationship(back_populates="document")


class Page(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    page_number: int
    page_text: str
    document_id: int | None = Field(default=None, foreign_key="document.id")
    document: Document | None = Relationship(back_populates="pages")
    bounding_boxes: list["BoundingBox"] | None = Relationship(back_populates="page")


class BoundingBox(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    word_text: str
    x: float
    y: float
    width: float
    height: float
    page_id: int | None = Field(default=None, foreign_key="page.id")
    page: Page | None = Relationship(back_populates="bounding_boxes")
