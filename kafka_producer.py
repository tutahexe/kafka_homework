import json

from kafka import KafkaProducer

folderName = "./kafka_certificates/"

service_uri = ""

producer = KafkaProducer(bootstrap_servers=service_uri,
                         security_protocol="SSL",
                         ssl_cafile=folderName + "ca.pem",
                         ssl_certfile=folderName + "service.cert",
                         ssl_keyfile=folderName + "service.key",
                         value_serializer=lambda v: json.dumps(v).encode('ascii'),
                         key_serializer=lambda v: json.dumps(v).encode('ascii'))

producer.send("test", key={"key": 1}, value={"URL": "https://aiven.io/"})

producer.flush()
