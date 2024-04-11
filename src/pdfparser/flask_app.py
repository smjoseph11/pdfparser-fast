from flask import Flask, jsonify, request
from sqlmodel import create_engine, SQLModel
from pdfparser import sqlmodel
from sqlalchemy.orm import sessionmaker

from pdfparser import config
from pdfparser.services import PDFService

app = Flask(__name__)
Session = sessionmaker()


@app.route("/parse_pdf", methods=["POST"])
def parse_pdf():
    data = request.json
    if "file_path" not in data:
        return jsonify({"message": "File path and PDF ID are required"}), 400

    file_path = data["file_path"]
    engine = create_engine(config.get_postgres_uri())
    SQLModel.metadata.create_all(engine)
    Session.configure(bind=engine)
    session = Session()
    try:
        pdfservice = PDFService(file_path)
        # create context manager for pdf parsing
        with pdfservice as pdfservice:
            document = pdfservice.create_document()
            session.add(document)
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


if __name__ == "__main__":
    app.run(debug=True)
