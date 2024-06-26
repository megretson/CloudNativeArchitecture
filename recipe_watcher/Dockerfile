FROM python:3-alpine

# ENV AWS_SHARED_CREDENTIALS_FILE=/root/.aws/credentials
# ENV AWS_CONFIG_FILE=/root/.aws/config
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 8080

CMD ["python3", "-u", "recipe_watcher.py"]