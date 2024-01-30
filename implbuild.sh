#!/bin/bash

sudo docker build -t dgodfrey206/python-server:v0.2.5 . &&
sudo docker push     dgodfrey206/python-server:v0.2.5   &&
nano config.yaml &&
kubectl apply -f config.yaml
