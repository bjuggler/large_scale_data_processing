# https://github.com/jonashaag/prometheus-multiprocessing-example/blob/master/yourapp.py
from flask import Flask, Response
from prometheus_client import multiprocess
from prometheus_client import generate_latest, CollectorRegistry, CONTENT_TYPE_LATEST


app = Flask(__name__)


@app.route("/metrics")
def metrics():
    collector_registry = CollectorRegistry()
    multiprocess.MultiProcessCollector(collector_registry)
    data = generate_latest(collector_registry)
    return Response(data, mimetype=CONTENT_TYPE_LATEST)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8088)