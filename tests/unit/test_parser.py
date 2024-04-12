from pathlib import Path

from pdfparser.services import PDFService

TEST_DATA = Path(__file__).parent.parent / "test_data"


def test_create_document_success():
    """This test ensures if we can read metadata from a pdf,
    count the pages, and create a Document object"""
    with PDFService(TEST_DATA / "Test_PDF.pdf") as pdfservice:
        document_record = pdfservice.create_document()
        print(document_record.document_name)
        assert document_record.document_name == "Test_PDF"
        assert document_record.total_pages == 1


def test_parse_pdf_success():
    """This test ensures we can create the appropriate Page objects associated with a Document"""
    with PDFService(TEST_DATA / "Test_PDF_2p.pdf") as pdfservice:
        document_record = pdfservice.create_document()
        document_record.id = 1
        list_of_pages = pdfservice.parse_pdf(document_record)
        # ensure page number starts at 1
        assert list_of_pages[0].page_number == 1
        assert list_of_pages[1].page_number == 2
        assert list_of_pages[0].page_text.strip() == "Test PDF with 2 pages"


def test_parse_page_word_success():
    """This test ensures we can load each space separated word
    into the word models and also load the corresponding bounding box information"""

    # Create an instance of PDFService
    with PDFService(TEST_DATA / "Test_PDF_2p.pdf") as pdfservice:
        document_record = pdfservice.create_document()
        document_record.id = 1
        list_of_pages = pdfservice.parse_pdf(document_record)
        page1 = list_of_pages[0]
        page1.id = 1

        bounding_boxes = pdfservice.parse_page(page1)

        assert bounding_boxes[0]
