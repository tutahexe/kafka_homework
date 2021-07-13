import json

from kafka import KafkaConsumer

folderName = "./kafka_certificates/"
service_uri = ""

consumer = KafkaConsumer(bootstrap_servers=service_uri,
                         security_protocol="SSL",
                         ssl_cafile=folderName + "ca.pem",
                         ssl_certfile=folderName + "service.cert",
                         ssl_keyfile=folderName + "service.key",
                         value_deserializer=lambda v: json.loads(v.decode('ascii')),
                         auto_offset_reset='latest'
                         )

consumer.subscribe("test")

for message in consumer:
    print(message)
