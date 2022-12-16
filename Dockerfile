FROM python:3.11.1

ADD . /app

COPY . .

# ENV GLIBC_REPO=https://github.com/sgerrand/alpine-pkg-glibc

WORKDIR /app

RUN pip install -r requirements.txt

CMD python app.py

