import argparse
import re
from time import sleep

import requests

from db.db_connector import write_data_to_db, init_db
from utilities import read_value_from_config
from kafka_builders.kafka_consumer import create_consumer
from kafka_builders.kafka_producer import create_producer


def check_url(url, pattern=None):
    """
    Check provided url for response, status code and regexp pattern
    :param url: website url
    :param pattern: regular expression pattern
    :return: Status code, time for response, is regexp pattern present
    """
    response = requests.get(url)
    st_code = response.status_code
    time = (response.elapsed.total_seconds())
    body = response.text
    reg_exp = False
    if pattern:
        search = re.search(pattern, body, re.IGNORECASE)
        if search:
            reg_exp = True
    return st_code, time, reg_exp


def producer_sender(producer, topic, url, st_code, time, reg_exp):
    """
    Build and send message to kafka.
    """
    producer.send(topic,
                  key={"key": 1},
                  value={"url": url, "status_code": st_code, "elapsed_time": time, "found_reg_exp": reg_exp}
                  )
    producer.flush()


def producer_loop(url, producer, timeout, topic, pattern):
    """
    Producer loop. Endless loop to check website for data and send this message to the Kafka.
    """
    while True:
        status_code, elapsed_time, reg_exp = check_url(url, pattern)
        producer_sender(producer, topic, url, status_code, elapsed_time, reg_exp)
        sleep(timeout)


def consumer_loop(consumer):
    """
    Consumer loop. Reads messages and stores them into DB.
    """
    for message in consumer:
        message_data = message.value
        write_data_to_db(message_data["url"], message_data["elapsed_time"], message_data["status_code"],
                         message_data["found_reg_exp"])


def main():
    """
    Main loop. Parses arguments to provide instance of consumer or producer with all necessary data.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--consumer', action='store_true')
    parser.add_argument('--producer', action='store_true')
    parser.add_argument('--init', action='store_true')
    args = parser.parse_args()
    kafka = read_value_from_config('kafka_connection')
    timeout = read_value_from_config('timeout')
    topic = read_value_from_config('topic')
    url = read_value_from_config('site')
    pattern = read_value_from_config('regexp_pattern')
    if args.init:
        init_db()
    if args.producer:
        producer = create_producer(kafka)
        producer_loop(url, producer, timeout, topic, pattern)
    elif args.consumer:
        consumer = create_consumer(kafka)
        consumer.subscribe(topic)
        consumer_loop(consumer)


if __name__ == '__main__':
    main()
