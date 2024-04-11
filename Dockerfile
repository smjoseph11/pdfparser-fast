# Use the official Python image as a base
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       curl \
       && apt-get clean \
       && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install poetry

# Set up Poetry environment variables
ENV PATH="/root/.poetry/bin:${PATH}"

# Copy only the necessary files
COPY pyproject.toml poetry.lock /app/

# Set the working directory
WORKDIR /app

# Install project dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev

# Copy the application code
COPY src /app/src
COPY tests /app/tests
COPY data /app/data
ENV PYTHONPATH=/app/src


# Run your application
CMD ["sh", "-c", "poetry run python src/pdfparser/flask_app.py && python src/pdfparser/create_tables.py"]
