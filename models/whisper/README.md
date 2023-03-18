## Running the model

To start the server on local machine, run

```
python3 main.py
```

## To run the docker image

```
docker run --rm -it -p 8080:8080 annanay25/nautical-whisper:latest
```

## Query the model / call the model API

The model is accessible at `https://localhost:8080`. The below screenshot shows how to query it using [Postman](https://www.postman.com/).

> Note: Model works only with `POST` requests.

![Querying](postman-bert-base-uncased.png)

## Prometheus metrics for API request time

Prometheus metrics are accessible at `https://localhost:8080/metrics`.

![Prometheus Metrics](./prom-metrics.png)