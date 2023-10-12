#!/bin/bash
#Arguments: 1.path 2.address 3.port

sudo docker image build -t file_monitor ./
sudo docker run -it -v /:/docker/host_root file_monitor python3 main.py --path=/docker/host_root"$1" --address="$2" --port="$3"