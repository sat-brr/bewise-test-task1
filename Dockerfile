FROM python:3.10

WORKDIR /code/
COPY . .

ENV PYTHONBUFFERED=1

RUN pip install --upgrade pip && pip install -r requirements.txt

ENV PYTHONPATH /code/