# from sqlalchemy import Column, Float, ForeignKey, Integer, MetaData, String, Table
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import registry, relationship

# from pdfparser import model

# registry = registry()
# Base = declarative_base()
# metadata = MetaData()

# documents = Table(
#     "documents", Base.metadata, Column("pdf_id", Integer, primary_key=True, autoincrement=True), Column("_name", String)
# )

# pages = Table(
#     "pages",
#     Base.metadata,
#     Column("page_id", Integer, primary_key=True, autoincrement=True),
#     Column("pdf_id", Integer, ForeignKey("documents.pdf_id")),
#     Column("page_number", Integer),
# )

# bounding_boxes = Table(
#     "bounding_boxes",
#     Base.metadata,
#     Column("bounding_box_id", Integer, primary_key=True, autoincrement=True),
#     Column("page_id", Integer, ForeignKey("pages.page_id")),
#     Column("word_text", String),
#     Column("x", Float),
#     Column("y", Float),
#     Column("width", Float),
#     Column("height", Float),
# )

# registry.map_imperatively(model.Document, documents, properties={"pages": relationship(model.Page, back_populates="document")})

# registry.map_imperatively(
#     model.Page,
#     pages,
#     properties={
#         "document": relationship(model.Document, back_populates="pages"),
#         "bounding_boxes": relationship(model.BoundingBox, back_populates="page"),
#     },
# )

# registry.map_imperatively(
#     model.BoundingBox, bounding_boxes, properties={"page": relationship(model.Page, back_populates="bounding_boxes")}
# )
