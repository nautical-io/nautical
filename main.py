#!/usr/bin/env python3
# ^ needed for Dockerfile

from http.server import BaseHTTPRequestHandler, HTTPServer
from models.BertBaseUncased import BertBaseUncased

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text")
        self.end_headers()
        self.wfile.write(bytes(str(BertBaseUncased("Hello I'm a [MASK] model.")), "utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
