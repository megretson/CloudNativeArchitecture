FROM python:3-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY client /usr/src/app/client
COPY requirements.txt /usr/src/app/
RUN pip3 install --no-cache-dir -r requirements.txt

# RUN python3 client/setup.py install 

COPY . /usr/src/app

ENV AWS_DEFAULT_REGION=us-east-2

EXPOSE 8081

# ENTRYPOINT ["python3"]

CMD ["python3", "-u", "recipe_sender.py"]