from sfisop.messaging_sdk.publisher import PublisherClient
from sfisop.messaging_sdk.configuration import ClientConfiguration, get_config_file

if __name__ == '__main__':

    config_file = get_config_file()

    config = ClientConfiguration(config_file)

    publisher_client = PublisherClient(config)

    publisher_client.publish_one("Hello World Publisher Client")