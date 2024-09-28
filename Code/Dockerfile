FROM python:3.8-slim-buster

WORKDIR /app

COPY . /app

RUN pip install Flask

EXPOSE 5000

ENV FLASK_APP=test.py

CMD ["flask", "run", "--host=0.0.0.0"]

