#!/usr/bin/env python3
# ^ needed for Dockerfile

from http.server import BaseHTTPRequestHandler, HTTPServer
from BertBaseUncased import BertBaseUncased
import os
import json

hostName = "0.0.0.0"
serverPort = 8080
contentLengthHeaderName = "content-length"


class MyServer(BaseHTTPRequestHandler):

    # do_POST gives access to the "content-length" header
    def do_POST(self):
        # parse the request and extract query
        req_body = self.rfile.read(int(self.headers.get(contentLengthHeaderName)))
        message = json.loads(req_body)

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        # this is some magic - apparently parameters are stored as "self.server.xxx"
        self.wfile.write(
            bytes(str(self.server.model(message['query'])), "utf-8")
        )


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    webServer.model = BertBaseUncased

    # this will run the model on an empty string - forcing it to download
    # weights from the huggingface hub the first time
    BertBaseUncased("[MASK]")

    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
