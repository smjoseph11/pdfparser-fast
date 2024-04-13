import fitz

from pdfparser import model


class PDFService:
    def __init__(self, file_path):
        self.file_path = file_path
        self.pdf_document = None

    def create_document(self):
        total_pages = self.pdf_document.page_count
        document_name = self.pdf_document.metadata.get("title", "Untitled")
        document_record = model.Document(document_name=document_name, total_pages=total_pages)
        return document_record

    def parse_pdf(self, document):
        try:
            page_list = []
            for page_number in range(document.total_pages):
                page = self.pdf_document.load_page(page_number)
                text = page.get_text()
                # fulfills requirement to remove newlines on page text
                text = text.replace("\n", " ")
                page_record = model.Page(pdf_id=document.id, page_number=page_number + 1, page_text=text)
                page_list.append(page_record)
            return page_list
        except Exception as e:
            raise ValueError(str(e))

    def parse_page(self, page):
        bounding_boxes = []
        # kind of ugly having to subtract 1 from the page number to load it here...
        fitz_page = self.pdf_document.load_page(page.page_number - 1)
        words_info = fitz_page.get_text("words")

        for word_info in words_info:
            word_text = word_info[4]  # Extract the text of the word
            word_bbox = fitz.Rect(word_info[:4])  # Bounding box of the word
            # Create BoundingBox instances for each word and add to the list
            bounding_boxes.append(
                model.BoundingBox(
                    word_text=word_text, x=word_bbox.x0, y=word_bbox.y0, width=word_bbox.width, height=word_bbox.height
                )
            )
        return bounding_boxes

    def __enter__(self):
        self.pdf_document = fitz.open(self.file_path)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.pdf_document:
            self.pdf_document.close()
