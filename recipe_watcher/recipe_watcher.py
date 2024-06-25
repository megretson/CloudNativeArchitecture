import json
import os
import threading
import pprint
import boto3
from botocore.exceptions import ClientError
import logging
import time
import pika
import sys

logger = logging.getLogger(__name__)


class RecipeWatcher:

    def __init__(self, polling_time=None) -> None:
        self.s3_resource = boto3.resource("s3")
        self.buckets = {
            bucket.name: bucket for bucket in self.s3_resource.buckets.all()}
        self.previous_files = None
        self.polling_time = polling_time if polling_time != None else 5
        connection = pika.BlockingConnection(
            pika.ConnectionParameters('localhost'))
        self.channel = connection.channel()
        self.channel.queue_declare(queue="recipe_jobs")

    def hello_s3(self):
        """
        Use the AWS SDK for Python (Boto3) to create an Amazon Simple Storage Service
        (Amazon S3) resource and list the buckets in your account.
        This example uses the default settings specified in your shared credentials
        and config files.
        """
        print("Hello, Amazon S3! Let's list your buckets:")
        for bucket in self.buckets.keys():
            print(f"\t{bucket}")

    def get_bucket(self, bucket_name):
        return self.buckets[bucket_name]

    def get_object_data(self, object):
        """
        Gets the object.

        :return: The object data in bytes.
        """
        try:
            body = object.get()["Body"].read().decode('utf-8')
            logger.info(
                "Got object '%s' from bucket '%s'.",
                object.key,
                object.bucket_name,
            )
        except ClientError:
            logger.exception(
                "Couldn't get object '%s' from bucket '%s'.",
                object.key,
                object.bucket_name,
            )
            raise
        except UnicodeDecodeError:
            logger.exception(
                "Couldn't get decode '%s' from bucket '%s'.",
                object.key,
                object.bucket_name,
            )
            raise
        else:
            return body

    def list_objects(self, bucket, prefix=None, unique=False):
        """
        Lists the objects in a bucket, optionally filtered by a prefix.

        :param bucket: The bucket to query. This is a Boto3 Bucket resource.
        :param prefix: When specified, only objects that start with this prefix are listed.
        :return: The list or set of objects.
        """
        try:
            if not prefix:
                if unique:
                    objects = set(bucket.objects.all())
                else:
                    objects = list(bucket.objects.all())
            else:
                if unique:
                    objects = set(bucket.objects.filter(Prefix=prefix))
                else:
                    objects = list(bucket.objects.all())
            logger.info(
                "Got objects %s from bucket '%s'", [
                    o.key for o in objects], bucket.name
            )
        except ClientError:
            logger.exception(
                "Couldn't get objects for bucket '%s'.", bucket.name)
            raise
        else:
            return objects

    def list_unique_objects(self, bucket, prefix=None):
        """
        Lists the objects in a bucket, optionally filtered by a prefix.

        :param bucket: The bucket to query. This is a Boto3 Bucket resource.
        :param prefix: When specified, only objects that start with this prefix are listed.
        :return: The list of objects.
        """
        return self.list_objects(bucket, None, True)

    def submit_new_objects(self, new_files: set):
        for file in new_files:
            data = self.get_object_data(file)
            pprint.pp(json.loads(data))
            self.enqueue_send_job(data)

    def enqueue_send_job(self, data):
        self.channel.basic_publish(exchange='',
                                   routing_key='recipe_jobs',
                                   body=data)

    def check_for_new_files(self, bucket):
        if self.previous_files:
            objects = self.list_unique_objects(bucket)
            if len(objects - self.previous_files) > 0:
                self.submit_new_objects(objects - self.previous_files)
                self.previous_files = objects
        else:
            self.previous_files = self.list_unique_objects(bucket)
        pass

    def poll_for_new_files(self, bucket):
        logger.info("Starting polling for new files")
        while (True):
            print("Polling")
            self.check_for_new_files(bucket)
            time.sleep(self.polling_time)


if __name__ == "__main__":
    file_watcher = RecipeWatcher()
    file_watcher.hello_s3()
    bucket = file_watcher.get_bucket("cloud-native-class-bucket")

    try:
        x = threading.Thread(
            target=file_watcher.poll_for_new_files, args=(bucket,), daemon=True)
        x.start()
        while x.is_alive():
            x.join(1)
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
