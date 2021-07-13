import argparse

from utilities import read_value_from_config
from kafka_builders.kafka_consumer import create_consumer
from kafka_builders.kafka_producer import create_producer


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--consumer', action='store_true')
    parser.add_argument('--producer', action='store_true')
    args = parser.parse_args()
    kafka = read_value_from_config('kafka_connection')
    if args.producer:
        producer = create_producer(kafka)
        producer.send("test", key={"key": 1}, value={"URL": "https://aiven.io/"})
        producer.flush()
    elif args.consumer:
        consumer = create_consumer(kafka)
        consumer.subscribe("test")
        for message in consumer:
            print(message)


if __name__ == '__main__':
    main()
