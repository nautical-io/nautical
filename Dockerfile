FROM python:3.10-slim-bullseye

RUN rm -rf /usr/local/cuda/lib64/stubs

COPY requirements.txt /

RUN pip install -r requirements.txt

ENV USE_TORCH=1

COPY main.py /usr/local/bin/

RUN chmod +x /usr/local/bin/main.py

ENTRYPOINT [ "/usr/local/bin/main.py" ]
