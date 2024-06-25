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
        self.configuration = openapi_client.Configuration(
            host="http://localhost:8080/MargaretAnderson/RecipeComparer/1.0.0"
        )
        self.polling_time = polling_time if polling_time != None else 5
        connection = pika.BlockingConnection(
            pika.ConnectionParameters('localhost'))
        self.channel = connection.channel()
        self.channel.queue_declare(queue="recipe_jobs")
        self.channel.basic_consume(queue='recipe_jobs',
                                   auto_ack=True,
                                   on_message_callback=self.callback)

    def start(self):
        print(' [*] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()

    def callback(self, ch, method, properties, body):
        print(f" [x] Received {body}")

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
                print("Successfully submitted recipe")

            except ApiException as e:
                print("Exception when calling DefaultApi->add_recipe: %s\n" % e)
            except ConnectionRefusedError as e:
                print("Connection Refused when calling DefaultApi->add_recipe: %s\n" % e)
            except Exception as e:
                print("Connection Refused when calling DefaultApi->add_recipe: %s\n" % e)

if __name__ == "__main__":
    try:
        recipe_sender = RecipeSender()
        recipe_sender.start()

    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
