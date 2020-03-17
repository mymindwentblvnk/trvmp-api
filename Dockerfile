FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

ENV DATABASE_URL sqlite:///

WORKDIR /

COPY ./app /app

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
