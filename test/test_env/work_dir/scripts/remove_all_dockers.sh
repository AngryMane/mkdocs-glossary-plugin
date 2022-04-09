#!/usr/bin/env bash
sudo docker rm -f `sudo docker ps -a -q`
sudo docker images -aq | xargs sudo docker rmi