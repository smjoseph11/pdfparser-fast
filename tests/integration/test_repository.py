from pathlib import Path

from pdfparser.model import Document, Page
from pdfparser.services import PDFService

TEST_DATA = Path(__file__).parent.parent / "test_data"


def test_load_document_into_sqlite_db(session):
    """Test case to verify loading a PDF document into an SQLite database."""
    pdfparser = PDFService(TEST_DATA / "Test_PDF.pdf")
    with pdfparser as pdfparser:
        document = pdfparser.create_document()
    session.add(document)
    session.commit()
    document = session.query(Document).first()
    assert document.document_name == "Test_PDF"


def test_load_pages_from_a_document(session):
    """Test loading pages from a PDF document into the database."""
    pdfparser = PDFService(TEST_DATA / "Test_PDF_2p.pdf")
    with pdfparser as pdfparser:
        document = pdfparser.create_document()
        session.add(document)
        session.commit()
        list_of_pages = pdfparser.parse_pdf(document)
        assert len(list_of_pages) == 2
        assert list_of_pages[0].page_text.strip() == "Test PDF with 2 pages"


def test_load_bounding_boxes_from_page(session):
    """Test loading bounding boxes from page of a PDF document."""
    pdfparser = PDFService(TEST_DATA / "Test_PDF_2p.pdf")
    with pdfparser as pdfparser:
        document = pdfparser.create_document()
        session.add(document)
        session.commit()
        list_of_pages = pdfparser.parse_pdf(document)
        session.add_all(list_of_pages)
        session.commit()
        page = session.query(Page).filter_by(page_number=1).first()
        bounding_boxes = pdfparser.parse_page(page)  # parsing the first page
        bounding_boxes[0].word_text = "Test"
