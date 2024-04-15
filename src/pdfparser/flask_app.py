from flask import Flask, jsonify, request
from sqlalchemy.orm.exc import NoResultFound
from sqlmodel import Session, select
from pdfparser.create_tables import create_tables
from pdfparser.model import Document, Page

from pdfparser import config
from pdfparser.services import PDFService

app = Flask(__name__)
engine = create_tables()

@app.route("/parse_pdf", methods=["POST"])
def parse_pdf():
    data = request.json
    if "file_path" not in data:
        return jsonify({"message": "File path required"}), 400

    file_path = data["file_path"]
    # Create all tables
    session = Session(engine)
    try:
        pdfservice = PDFService(file_path)
        # create context manager for pdf parsing
        with pdfservice as pdfservice:
            document = pdfservice.create_document()
            session.add(document)
            session.commit()
            page_list = pdfservice.parse_pdf(document)
            session.add_all(page_list)
            session.commit()
            for page in page_list:
                bounding_boxes = pdfservice.parse_page(page)
                session.add_all(bounding_boxes)
                session.commit()
        return jsonify({"message": f"{len(page_list)} pages parsed successfully"}), 201
    except ValueError as e:
        return jsonify({"message": str(e)}), 500
    finally:
        session.close()

@app.route("/print_page", methods=["GET"])
def print_page():
    data = request.json
    if "document_name" not in data:
        return jsonify({"message": "Document name required"}), 400

    document_name = data["document_name"]
    session = Session(engine)
    try:
        # Retrieve the PDF document based on the document name and PDF ID
        stmt = select(Document).where(Document.document_name == document_name)
        document = session.execute(stmt).scalar_one_or_none()
        if not document:
            return jsonify({"message": "PDF not found"}), 404
        
        # Retrieve the specified page from the PDF document
        page_number = request.args.get("page_number") 
        page: Page = session.query(Page).filter(Page.document_id == document.id, Page.page_number == page_number).one_or_none()
        if not page:
            return jsonify({"message": f"Page {page_number} not found for the specified PDF"}), 404
        
        # Return the content of the page
        return jsonify({"content": page.page_text}), 200
    except NoResultFound:
        return jsonify({"message": "Resource not found"}), 404
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    finally:
        session.close()


if __name__ == "__main__":
    app.run(debug=True)
