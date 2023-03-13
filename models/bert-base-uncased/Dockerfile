FROM python:3.10-slim-bullseye

RUN rm -rf /usr/local/cuda/lib64/stubs

COPY requirements.txt /

RUN pip install -r requirements.txt

ENV USE_TORCH=1

WORKDIR /home/nautical

COPY main.py BertBaseUncased.py __init__.py /home/nautical/

RUN chmod +x /home/nautical/main.py

ENTRYPOINT [ "/home/nautical/main.py" ]
