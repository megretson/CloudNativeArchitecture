FROM python:3-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

ENV AWS_DEFAULT_REGION=us-east-2

EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["-m", "openapi_server"]