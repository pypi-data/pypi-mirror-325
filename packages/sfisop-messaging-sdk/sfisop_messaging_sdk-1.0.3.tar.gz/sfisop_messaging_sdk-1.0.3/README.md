# Messaging Service Client SDK

Client library for accessing the realtime messaging services of the SmartOcean platform.

The messaging services rely on the [MQTT Standard](https://mqtt.org/) 

This client SDK implementation utilises the [Paho MQTT](https://pypi.org/project/paho-mqtt/) library. The Paho MQTT library may also be used directly to access the messaging services in case more advanced use is required.

## Credentials

Credentials for accessing the messaging service being consumed must be placed in a `.env` file with the following content

```
BROKER_USERNAME=<username>
BROKER_PASSWORD=<password>
```

## Configuration

Broker configuration information must be provided in a yaml configuration file with the following format:

```
BROKER_HOST: 
BROKER_PORT: 
BROKER_TOPIC: 
TOPIC_QOS: 
CLIENT_ID: 
```
The name of the configuration file in the example below is to be provided as a command-line argument when running the Python application.

## Sample Subscriber

A sample implementation accessing the messaging service as a subscriber:

```python

import sfisop.messaging_sdk.subscriber as mqtt_subscriber
import sfisop.messaging_sdk.configuration as mqtt_configuration

import logging

logging.basicConfig(filename='subscriber_client.log',
                    format="%(asctime)s[%(levelname)s]:%(message)s", encoding='utf-8',
                    level=logging.DEBUG)

logging.info("MQTT Subscriber Client module")


class DataConsumer(mqtt_subscriber.SubscriberClient):

    def __init__(self, config_file : str):

        mqtt_client_config = mqtt_configuration.ClientConfiguration(config_file)

        super().__init__(mqtt_client_config)

    def process_one(self, in_message):

        logging.info(f'Data Consumer process_one: {in_message}')


if __name__ == '__main__':

    config_file = mqtt_configuration.get_config_file()

    data_consumer = DataConsumer(config_file)

    data_consumer.run()
```

## Sample Publisher

A sample implementation accessing the messaging service as a publisher:

```python
from sfisop.messaging_sdk.publisher import PublisherClient
from sfisop.messaging_sdk.configuration import ClientConfiguration, get_config_file

if __name__ == '__main__':

    config_file = get_config_file()

    config = ClientConfiguration(config_file)

    publisher_client = PublisherClient(config)

    publisher_client.publish_one("Hello World Publisher Client")
```


