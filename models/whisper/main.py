#!/usr/bin/env python3
# ^ needed for Dockerfile

from http.server import BaseHTTPRequestHandler, HTTPServer
from Whisper import Whisper
from prometheus_client import generate_latest, Summary, REGISTRY
import json

hostName = "0.0.0.0"
serverPort = 8080
contentLengthHeaderName = "content-length"
# metric to track time spent and requests made.
REQUEST_TIME = Summary("request_processing_seconds", "Time spent processing request")


class MyServer(BaseHTTPRequestHandler):
    # do_GET needed for Prometheus metrics
    def do_GET(self):
        if self.path == "/metrics":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(generate_latest(REGISTRY))

    # do_POST gives access to the "content-length" header
    @REQUEST_TIME.time()
    def do_POST(self):
        # parse the request and extract query
        req_body = self.rfile.read(int(self.headers.get(contentLengthHeaderName)))
        message = json.loads(req_body)

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        # this is some magic - apparently parameters are stored as "self.server.xxx"
        self.wfile.write(bytes(str(self.server.model(message["query"])), "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    webServer.model = Whisper

    # FIXME: force run the model
    Whisper("[MASK]")

    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
