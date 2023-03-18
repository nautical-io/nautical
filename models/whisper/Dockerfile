FROM python:3.10-slim-bullseye

RUN apt update -y && apt install -y ffmpeg

COPY requirements.txt /

RUN pip install -r requirements.txt

ENV USE_TORCH=1

WORKDIR /home/nautical

COPY main.py test-data/lachlan_evenson.mp3 /home/nautical/

RUN chmod +x /home/nautical/main.py &&\
    mkdir -p /home/nautical/uploads

ENTRYPOINT [ "/home/nautical/main.py" ]
