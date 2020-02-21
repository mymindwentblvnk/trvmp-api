# trvmp-api
FIFA Dashboard based on FastAPI.

## Docker

### Build
`docker build -t trvmp .`

### Run
`docker run --name trvmp -p 80:80 trvmp`

## Local

### Run
`uvicorn app.main:app --reload`

### PEP 8
`flake8`