FROM ubuntu:20.04
USER root

ENV TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update
RUN apt-get -y install software-properties-common wget git python3-setuptools curl 


RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update
RUN apt-get -y install python3.7
#RUN apt-get -y install python3.8
RUN apt-get -y install python3.9
RUN apt-get -y install python3.10
