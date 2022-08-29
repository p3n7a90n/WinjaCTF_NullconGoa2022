FROM python:3.4

WORKDIR /app

# Python related files

COPY CVEData /app/CVEData/

COPY requirements.txt main.py app.py /app/

# Python3 http server and script to delete every 30 seconds

COPY entrypoint.sh  /app/

## flag

COPY flag /flag

RUN mkdir -p /var/www/

RUN pip3 install -r requirements.txt

RUN chmod +x /app/entrypoint.sh

RUN useradd -u 1000 -m FlaskServer

RUn chown -R FlaskServer /var/www/

USER FlaskServer

ENTRYPOINT ["./entrypoint.sh" ]



