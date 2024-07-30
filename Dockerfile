FROM python:3.9
WORKDIR /usr/src/techchallenge2mlet
COPY ./app ./app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt