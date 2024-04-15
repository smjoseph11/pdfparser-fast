# A PDF Parser written in Python using DDD and containerized with Docker
To run the containerized application:
```
docker-compose build
docker-compose up
docker exec {conainer_id} curl -X POST -H "Content-Type: application/json" -d '{"file_path": "data/wizard-of-oz.pdf"}' http://localhost:5000/parse_pdf
```