from decouple import config
import yaml

import argparse
import os


class ConfigurationException(Exception):
    pass


class ClientConfiguration:

    def __init__(self, config_file: str):

        try:
            self.USERNAME = config('BROKER_USERNAME')
            self.PASSWORD = config('BROKER_PASSWORD')

        except Exception as e:
            raise ConfigurationException(f"Error when reading credentials: {e}")

        try:
            with open(config_file) as f:
                conf = yaml.load(f, Loader=yaml.FullLoader)
                self.BROKER_HOST = conf['BROKER_HOST']
                self.BROKER_PORT = conf['BROKER_PORT']
                self.BROKER_TOPIC = conf['BROKER_TOPIC']
                self.TOPIC_QOS = conf['TOPIC_QOS']
                self.CLIENT_ID = conf['CLIENT_ID']

        except Exception as e:
            raise ConfigurationException(f"Error when reading from config file: {e}")

    def __str__(self) -> str:
        return ''.join((f'Publisher Client Configuration: \n',
                        f'BROKER TOPIC: {self.BROKER_TOPIC}:{self.TOPIC_QOS} \n',
                        f'BROKER: {self.BROKER_HOST}:{self.BROKER_PORT} \n',
                        f'CLIENT ID: {self.CLIENT_ID}'))


def get_config_file():

    parser = argparse.ArgumentParser()
    parser.add_argument("--configfile", required=True, help="Path to the config file")
    args = parser.parse_args()

    if not os.path.exists(args.configfile):
        raise ConfigurationException(f"Error: The configfile '{args.configfile}' does not exist.")

    return args.configfile
