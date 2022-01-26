import time
import json
from kafka import KafkaProducer
from configparser import ConfigParser
from crypto import APIService

cyber_log = initLogger()
config_file_path = getConfigPath()
kafka_config = ConfigParser()
kafka_config.read_file(open(f"{Path(__file__).parents[0]}/config.cfg"))
kafka_producer = kafka_config["producer.settings"]

kafka_topic = kafka_producer["topic"]
kafka_url = kafka_producer["url"]
kafka_timeout = int(kafka_producer["request.timeout.ms"])

# initializes kafka producer
producer = KafkaProducer(bootstrap_server = kafka_config["bootstrap_servers"]
                        value_serializer = lambda x: json.dumps(x).encode('utf-8'))

def produceMessage(filtered_json):
    for coin_data in filtered_json:
        coin_name = coin_data["name_coin"]

        # sends coin data to producer, 
        # if failed, write error to log
        try:
            producer.send(topic = kafka_topic,
                          key = coin_name,
                          value = coin_data)
        except Exception as error:
            cyber_log.error(f"Exception for coin {coin_name}: {error}")

if __name__ == "__main__":
    api = APIService()
    while True:
        original_json = api.getJson(kafka_url)
        filtered_json = api.filterJson(original_json)
        produceMessage(filtered_json)
        time.sleep(kafka_timeout)