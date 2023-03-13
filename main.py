#!/usr/bin/env python3
# ^ needed for Dockerfile

from http.server import BaseHTTPRequestHandler, HTTPServer
from models.BertBaseUncased import BertBaseUncased
import os

hostName = "0.0.0.0"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text")
        self.end_headers()
        # this is some magic - apparently parameters are stored as "self.server.xxx"
        self.wfile.write(bytes(str(self.server.model("Hello I'm a [MASK] model.")), "utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)

    model_name = os.environ['NAUTICAL_MODEL']
    if model_name == 'bert-base-uncased':
        webServer.model = BertBaseUncased
        # run this on an empty string so it downloads model weights the first time it starts
        BertBaseUncased("[MASK]")

    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
