
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
