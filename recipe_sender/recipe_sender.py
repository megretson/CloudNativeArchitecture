import json
import os
import sys
import threading
import openapi_client
from openapi_client.rest import ApiException
import logging
import time
import pika
from urllib3.exceptions import NewConnectionError
import queue_wrapper
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)


class RecipeSender:

    def __init__(self, polling_time=None) -> None:

        self.configuration = openapi_client.Configuration(
            host="recipe_server.cloud-pod-network/MargaretAnderson/RecipeComparer/1.0.0"
        )
        self.polling_time = polling_time if polling_time != None else 5
        self.queue = queue_wrapper.create_queue("CloudComputingMessagingQueue")

    def start(self):
        logger.info(' [*] Waiting for messages. To exit press CTRL+C')
        self.start_consuming()
    
    def unpack_message(self, msg):
        return json.loads(msg.body)

    def start_consuming(self):
        while True:
            received_messages = self.receive_messages(2)
            for message in received_messages:
                body = self.unpack_message(message)
                logger.info(f" [x] Received {body}")
                self.submit_data(body)
            if received_messages:
                self.delete_messages(received_messages)

    def submit_data(self, data):
        # # Enter a context with an instance of the API client
        with openapi_client.ApiClient(self.configuration) as api_client:
            # Create an instance of the API class
            api_instance = openapi_client.DefaultApi(api_client)
            recipe = openapi_client.Recipe.from_dict(data)

            try:
                # add a new recipe
                added_recipe = api_instance.add_recipe(recipe=recipe)
                logger.info("Successfully submitted recipe")

            except ApiException as e:
                logger.info("Exception when calling DefaultApi->add_recipe: %s\n" % e)
            except ConnectionRefusedError as e:
                logger.info("Connection Refused when calling DefaultApi->add_recipe: %s\n" % e)
            except Exception as e:
                logger.info("Connection Refused when calling DefaultApi->add_recipe: %s\n" % e)
    
    def receive_messages(self, max_number):
        """
        Receive a batch of messages in a single request from an SQS queue.

        :param queue: The queue from which to receive messages.
        :param max_number: The maximum number of messages to receive. The actual number
                            of messages received might be less.
        :param wait_time: The maximum time to wait (in seconds) before returning. When
                            this number is greater than zero, long polling is used. This
                            can result in reduced costs and fewer false empty responses.
        :return: The list of Message objects received. These each contain the body
                    of the message and metadata and custom attributes.
        """
        try:
            messages = self.queue.receive_messages(
                MessageAttributeNames=["All"],
                MaxNumberOfMessages=max_number,
                WaitTimeSeconds=self.polling_time,
            )
            for msg in messages:
                logger.info("Received message: %s: %s", msg.message_id, msg.body)
        except ClientError as error:
            logger.exception("Couldn't receive messages from queue: %s", queue)
            raise error
        else:
            return messages
    
    def delete_messages(self, messages):
        """
        Delete a batch of messages from a queue in a single request.

        :param queue: The queue from which to delete the messages.
        :param messages: The list of messages to delete.
        :return: The response from SQS that contains the list of successful and failed
                message deletions.
        """
        try:
            entries = [
                {"Id": str(ind), "ReceiptHandle": msg.receipt_handle}
                for ind, msg in enumerate(messages)
            ]
            response = self.queue.delete_messages(Entries=entries)
            if "Successful" in response:
                for msg_meta in response["Successful"]:
                    logger.info("Deleted %s", messages[int(msg_meta["Id"])].receipt_handle)
            if "Failed" in response:
                for msg_meta in response["Failed"]:
                    logger.warning(
                        "Could not delete %s", messages[int(msg_meta["Id"])].receipt_handle
                    )
        except ClientError:
            logger.exception("Couldn't delete messages from queue %s", queue)
        else:
            return response

if __name__ == "__main__":
    try:
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s",
            handlers=[logging.FileHandler("debug.log"), logging.StreamHandler(sys.stdout)],
        )
        logger.info('Hello Recipe Sender')
        recipe_sender = RecipeSender()
        recipe_sender.start()

    except KeyboardInterrupt:
        logger.info('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
