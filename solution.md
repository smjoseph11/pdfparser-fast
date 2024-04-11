---
name: "\U0001F41E Solution log/process"
about: This documents my thought processes and solutions to the exercise
---

# Process log

1. The first step is to get my environment correctly working.

    Because I am using WSL 2 I need to integrate Docker Desktop for Windows with this subsystem to use docker commands within it.

    https://docs.docker.com/go/wsl2/

    I will integrate the poetry configuration into a Dockerfile later on. 
    First I will get my local environment working.

2.  WSL's default Python3 version is 3.8^, this project requires 3.10^. I used pyenv to install 
python3.10 
    ```
    curl https://pyenv.run | bash

    export PATH="$HOME/.pyenv/bin:$PATH"
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"

    pyenv install 3.10
    ```
    I then change the poetry environment to this pyenv with `poetry env use /home/smjoseph11/miniconda3/bin/python` which is my local installation path for python3.10

3. I can now run `poetry run pre-commit run --all-files` to check the formatting of files regularly. If this was a true dev environment I would create a git hook with `poetry run pre-commit install` to run black, isort, mypy, and flake8 checks before commiting code into a repo

4. Based on the provided domain expectations, I create a domain model with Python classes. These classes are the Document, Page, Word, and BoundingBox classes. 

5. I don't like to entangle SQLAlchemy with my models (I learned from the CosmicPython pattern) so I use the SQLAlchemy mapper functionality to map my Python models to SQLAlchemy classes in the orm.py file

6. I have a one-to-many relationship between my Document and my Pages and a one-to-many relationship between my Pages and my Bounding Boxes. I can specify this relationship in SQLAlchemy using table relationships provided by SQLAlchemy

7. Now that I have completed the ORM and identified the appropriate relationships between my models, I have decided to continue with the service layer. This layer will perform the parsing of the PDF
    * To parse a PDF you first need to get the Document, then the Pages of the document, and the corresponding Bounding Box information for each Page. I have broken each of these steps up into 3 methods in the PDFService class
    * I have also decided to use a context manager to open and close the pdf

8. With the service layer complete, I moved onto creating a flask endpoint to call each one of these functions found in PDFServices, effectively filling a database with parsed information when a POST is called with a pdf file.

9. I then created a Dockerfile to containerize my application. I set some configurations up, install poetry, install dependencies, copy over working directories, and finally run my application
10. I then added a web service to the docker-compose for my application

To run the containerized application:
```
docker-compose build
docker-compose up
docker exec {conainer_id} curl -X POST -H "Content-Type: application/json" -d '{"file_path": "data/wizard-of-oz.pdf"}' http://localhost:5000/parse_pdf
```
You can run tests with `poetry run pytest`

NOTE:
Instead of using the schema.sql file I decided to use SQLalchemy's functionality as found in create_tables.py. I could have explicitly created the tables and relationships in the schema file instead.


# Creating the Domain
Whenever I approach domain-based projects I first consider the domain model. In this exercise, the domain model is written out in clear terms. I am writing a parser. I have deduced the following about how I will construct this parser:


* A PDF is identified by its name and the number of pages it contains.

    Each page within the PDF is identified by a page number and compromises multiple pages where each page has a corresponding document name. For example:

    100 pages of example.pdf

    We need to parse pages to a document. When we've parsed all pages of a document, we can consider another operation of our domain model. 

    For example, we can send this entry to an AI interpreter.

There are some things we should check to ensure this model sends accurate and atomic data.

1. We cannot parse a page without a corresponding document already in the database
2. We cannot parse a page number that has already been parsed
3. We cannot consider seeding of the DB complete unless the whole document is parsed (we will use some SQLAlchemy session atomicity (commit/rollback) to ensure this)
    NOTE: this is a design decision that ensures no data is lost. The other option is to send whatever could be parsed


