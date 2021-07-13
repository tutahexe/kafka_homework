import json

from kafka import KafkaConsumer

folderName = "./kafka_certificates/"


def create_consumer(bootstrap_servers=None):
    return KafkaConsumer(bootstrap_servers="kafka-35b85ff8-eposta-e940.aivencloud.com:22343",
                         security_protocol="SSL",
                         ssl_cafile=folderName + "ca.pem",
                         ssl_certfile=folderName + "service.cert",
                         ssl_keyfile=folderName + "service.key",
                         value_deserializer=lambda v: json.loads(v.decode('ascii')),
                         auto_offset_reset='latest'
                         )
