FROM ubuntu:22.04
WORKDIR /docker
RUN apt update && apt upgrade -y
RUN apt-get update
RUN apt install -y python3 python3-pip
RUN cd /docker
COPY ./ ./
RUN pip3 install -r requirements.txt
