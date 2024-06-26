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

logger = logging.getLogger(__name__)


class RecipeSender:

    def __init__(self, polling_time=None) -> None:

        # client = docker.from_env()
        # network_name = "uv_atp_network"
        # atp_container = client.containers.get(socket.gethostname())
        # client.networks.get(network_name).connect(container=atp_container.id)

        self.configuration = openapi_client.Configuration(
            host="http://localhost:8080/MargaretAnderson/RecipeComparer/1.0.0"
        )
        self.polling_time = polling_time if polling_time != None else 5
        connection = pika.BlockingConnection(
            pika.ConnectionParameters('172.17.0.2'))
        self.channel = connection.channel()
        self.channel.queue_declare(queue="recipe_jobs")
        self.channel.basic_consume(queue='recipe_jobs',
                                   auto_ack=True,
                                   on_message_callback=self.callback)

    def start(self):
        logger.info(' [*] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()

    def callback(self, ch, method, properties, body):
        logger.info(f" [x] Received {body}")

        self.submit_data(body)

    def submit_data(self, data):
        # # Enter a context with an instance of the API client
        with openapi_client.ApiClient(self.configuration) as api_client:
            # Create an instance of the API class
            api_instance = openapi_client.DefaultApi(api_client)
            d = json.loads(data)
            recipe = openapi_client.Recipe.from_dict(d)

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

if __name__ == "__main__":
    try:
        logger.info('Hello Recipe Sender')
        recipe_sender = RecipeSender()
        recipe_sender.start()

    except KeyboardInterrupt:
        logger.info('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
