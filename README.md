# Project description
Main goal is to create web-site checker which store data to the DB.
Since Producer and Consumer can be used in different environment, Kafka is used for communication.
# Project structure
* db\ - contains db related scripts
* kafka_builders\ - contains builders for consumer and producer
* .env - configuration file
* main.py - main file, all necessary actions/loops are done here
* utilities.py - at current point contains utility method to read data from env file
# Project installation
## Kafka configuration
You need to create kafka and postgres services in Aiven console.
Set `'kafka.auto_create_topics_enable'` to `'True'` and enable `'Kafka REST API (Karapace)'`
## Connection configuration
* Download all certificates from aiven console for Kafka ('ca.pem', 'service.cert' and 'service.key') and put them to 'kafka_ceritificates' directory.
* Create config file in root folder named ".env" with next structure:
```
{
    "db_connection" : "service_uri",
    "kafka_connection" : "service_uri",
    "topic": "testy",
    "site": "https://aiven.io/blog?posts=30&search=kafka",
    "regexp_pattern": "(saaa.*)",
    "timeout": 30
}
```
* db_connection - Service URI from aiven console (PostgreSQL)
* kafka_connection - Service URI from aiven console (Kafka)
* topic - topic used by consumer and producer for communication
* site - URL for check
* regexp_pattern - optional regular expression for validation
* timeout - timeout between checks
## Project configuration
From root folder run 'pip install -r requirements.txt'

# Running the project
* Create a table to store results: `main.py --init`
* Run consumer: `main.py --consumer`
* Run producer: `main.py --producer`