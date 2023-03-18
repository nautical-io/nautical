#!/usr/bin/env python3
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
model = whisper.load_model("base")

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
    file.save('./uploads/' + file.filename)
    print('File saved successfully')
    result = model.transcribe("./uploads/" + file.filename)
    return result["text"]

if __name__ == '__main__':
    model.transcribe("./lachlan_evenson.mp3")
    app.run(host=hostName, port=serverPort)
