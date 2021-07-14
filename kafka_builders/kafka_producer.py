import json
from kafka import KafkaProducer

folderName = "./kafka_certificates/"


def create_producer(bootstrap_servers=None):
    """
    :param bootstrap_servers: URI Kafka service
    :return: Kafka Producer
    """
    return KafkaProducer(bootstrap_servers=bootstrap_servers,
                         security_protocol="SSL",
                         ssl_cafile=folderName + "ca.pem",
                         ssl_certfile=folderName + "service.cert",
                         ssl_keyfile=folderName + "service.key",
                         value_serializer=lambda v: json.dumps(v).encode('ascii'),
                         key_serializer=lambda v: json.dumps(v).encode('ascii'))