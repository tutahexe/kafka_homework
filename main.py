import argparse

from db.db_writer import write_data
from utilities import read_value_from_config
from kafka_builders.kafka_consumer import create_consumer
from kafka_builders.kafka_producer import create_producer


def main():
    """
    Main loop. Parses arguments to provide instance of consumer or producer with all necessary data.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--consumer', action='store_true')
    parser.add_argument('--producer', action='store_true')
    args = parser.parse_args()
    kafka = read_value_from_config('kafka_connection')
    if args.producer:
        producer = create_producer(kafka)
        st_code = 500
        time = 0.1
        reg_exp = True
        producer.send("test", key={"key": 1}, value={"url": "https://aiven.io/", "status_code": st_code, "elapsed_time": time, "found_reg_exp": reg_exp})
        producer.flush()
    elif args.consumer:
        consumer = create_consumer(kafka)
        consumer.subscribe("test")
        for message in consumer:
            message_data = message.value
            write_data(message_data["url"], message_data["elapsed_time"], message_data["status_code"],
                       message_data["found_reg_exp"])


if __name__ == '__main__':
    main()
