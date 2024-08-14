import boto3
from botocore.exceptions import ClientError
import logging
import queue_wrapper
import json
import urllib.parse


print('Loading function')

s3 = boto3.client('s3')
queue = queue_wrapper.create_queue("CloudComputingMessagingQueue")
logger = logging.getLogger(__name__)


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        body = response["Body"].read().decode('utf-8')
        enqueue_send_job(body)
        logger.info(
            "Got object '%s' from bucket '%s'.",
            key,
            bucket,
        )
        print("CONTENT TYPE: " + response['ContentType'])
        return response['ContentType']
    
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
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e

def enqueue_send_job(data):
    send_messages([{"body": data, "attributes": {}}])


def send_messages(messages):
    """
    Send a batch of messages in a single request to an SQS queue.
    This request may return overall success even when some messages were not sent.
    The caller must inspect the Successful and Failed lists in the response and
    resend any failed messages.

    :param queue: The queue to receive the messages.
    :param messages: The messages to send to the queue. These are simplified to
                    contain only the message body and attributes.
    :return: The response from SQS that contains the list of successful and failed
            messages.
    """
    try:
        entries = [
            {
                "Id": str(ind),
                "MessageBody": msg["body"],
                "MessageAttributes": msg["attributes"],
            }
            for ind, msg in enumerate(messages)
        ]
        response = queue.send_messages(Entries=entries)
        if "Successful" in response:
            for msg_meta in response["Successful"]:
                logger.info(
                    "Message sent: %s: %s",
                    msg_meta["MessageId"],
                    messages[int(msg_meta["Id"])]["body"],
                )
        if "Failed" in response:
            for msg_meta in response["Failed"]:
                logger.warning(
                    "Failed to send: %s: %s",
                    msg_meta["MessageId"],
                    messages[int(msg_meta["Id"])]["body"],
                )
    except ClientError as error:
        logger.exception("Send messages failed to queue: %s", queue)
        raise error
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e
    else:
        return response

   