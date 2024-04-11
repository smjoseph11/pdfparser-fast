# Python Backend Challenge

Welcome to the Python Backend Challenge!!!!

The objective of this challenge is to create a pipeline to extract the text from the included pdf file and load it into a data store.

The goal of this challenge is to provide you an opportunity to express yourself as a Python developer and backend engineer.  

Outside of of the following key objectives, how you accomplish those objectives is completely up to you!

# Objectives

* Create a database schema for storing the following information about the data in the example PDF:
  * Document
    * document name
    * number of pages
  * Page
    * page number (1 indexed)
    * page text - All the text on the page, with newline information removed
    * bounding box information - The text and coordinates of every word on the page

* Create a pipeline/script to extract the text from the input data and load the above schema

# Requirements & Evaluation

You must use python to build your pipeline and postgres as your datastore.  All other choices of packages, tools, code design and organization, etc. are up to you.  

A few things we value in our own development practices are:

* Well tested code!!! Unit + integration tests with adequate coverage
* Simple, easy to read and manageable code
* Use of well supported tooling, <u>where appropriate</u>. (Example: Pydantic, SQLAlchemy, async, Django, etc...)
* Typing and consistent formatting
* Judicious use of comments and following standard conventions, without being overly Pydantic

# Submission

We have provided an empty SOLUTION.md where you can explain your design decisions and any other information you think we'd need to test/run/evaulate your code.  We'd like to know why you chose certain packages and tooling, reasoning behind your schema design, and any other details on your solution you'd deem important for us to know.

Please do NOT submit your code or challenge to a public github repository or other public location, helping us ensure the integrity of this challenge.  You can simply .zip up your solution and return via email correspondance.

# Setup

We have included a few provisions to help you get started more quickly, but you are not obligated to use any of it.  These include:

* `pyproject.toml/poetry.lock` - For creating a Poetry environment with some packages and tools we use at AlaffiaHealth.
* `docker-compose.yaml` - Will spin up a docker container running postgres and a database called `docs` and run any commands in schema.sql.
* `.pre-commit-config.yaml` - We use `pre-commit` in our Python repos
