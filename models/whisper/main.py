#!/usr/bin/env python3
# ^ needed for Dockerfile

from http.server import BaseHTTPRequestHandler, HTTPServer
# from Whisper import Whisper
from prometheus_client import generate_latest, Summary, REGISTRY
# import json
from flask import Flask, request, render_template
import whisper

hostName = "0.0.0.0"
serverPort = 8080
contentLengthHeaderName = "content-length"
# metric to track time spent and requests made.
REQUEST_TIME = Summary("request_processing_seconds", "Time spent processing request")

app = Flask(__name__)

# Define the route for the file upload page
@app.route('/')
def upload_file_page():
    return render_template('upload.html')

# Define the route for handling file uploads
@app.route('/metrics', methods=['GET'])
def return_metrics():
    return generate_latest(REGISTRY)

# Define the route for handling file uploads
@app.route('/upload', methods=['POST'])
@REQUEST_TIME.time()
def upload_file():
    file = request.files['file']
    # TODO: make sure this path exists
    file.save('./uploads/' + file.filename)
    model = whisper.load_model("base")
    result = model.transcribe("audio.mp3")
    print(result["text"])
    return 'File saved successfully'

if __name__ == '__main__':
    app.run(host=hostName, port=serverPort)
