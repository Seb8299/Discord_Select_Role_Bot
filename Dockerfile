# syntax=docker/Dockerfile:1.2
FROM ubuntu:22.04

COPY . /src
WORKDIR /src

RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get -y install python3 python3-pip
RUN python3 -m pip install -U discord.py

CMD ["/usr/bin/python3", "/src/main.py"]
