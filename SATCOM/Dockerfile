FROM python:3.8

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY Certs/ /app/Certs/

COPY app.py main.py flag.txt websocket.py /app/

RUN useradd -u 1000 -m pythonServer

USER pythonServer

ENTRYPOINT [ "python3" ]

CMD ["main.py" ]
