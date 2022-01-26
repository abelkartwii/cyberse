# Cyber Stockholm Syndrome
## Overview
This project uses Kafka, Spark Streaming, and Cassandra (in a dockerized environment) to fetch real-time cryptocurrency prices and information.

Project name inspired by Rina Sawayama's song [Cyber Stockholm Syndrome]().

## Configuration
All necessary tools and packages are listed in the `docker-compose.yml` that can be run in Docker. To do so, make sure you have Docker and Docker Compose installed.

To run, navigate to the project directory and use the command `docker-compose up`, which will retrieve and publish the desired information. To start services, run `start-services.sh` in the project directory. To stop services, run `docker-compose down`.

If Docker is not an option, scroll to the end for manual configuration with all the required tools listed. :)

## Approach
**Fetching real-time data** (Kafka)
A Kafka producer is used to fetch and parse the JSON data in real-time from the [Coinranking API](https://coinranking.com/page/cryptocurrency-api). Once parsed, the data will be filtered to only include the necessary fields, and then the filtered data will be sent to a Kafka topic.



## Manual configuration
To run without Docker, you will need:
* [Python](https://www.python.org/downloads/) 3.9.2
* [Apache Spark](https://spark.apache.org/downloads.html) 3.0.1 (namely PySpark and Spark Streaming)
* [Apache Kafka](https://kafka.apache.org/downloads) 2.7.0
* [Apache Cassandra](https://cassandra.apache.org/download/) 3.11
