# Welcome to File_Monitoring_Mqtt_Update repository

## Getting Started

These instructions will get you a copy of the project up and running on your 
local machine for development and testing purposes.

### Prerequisites

Linux OS

Python 3 should be installed (>= 3.8.0). 

And the following pip packages as well

* pyinotify

* paho-mqtt

* datetime

* argparse

Dockerfile is also given with the required dependencies pre-installed, to run this project


## Objective

Defined File/Directory is monitored for change events. 

In case of Changes, event_type, file/directory type, timestamp of event is published
onto a mqtt topic which is the absolute path to the changed file.

Path of File/Directory to be monitored, Mqtt Broker address and port to be 
specified during execution


## Execution

### Demonstration Video is included on 00_Demo.zip

This project can be executed

* by directly calling the main.py package 
 
e.g. python3 main.py --path=/PATH/TO/BE/MONITORED --address=mqttbrokeraddress --port=mqttbrokerport

 python3 main.py --path=/home/rkumarv/test --address=mqtt.eclipseprojects.io --port=1883

This will executed main.py file directly onto machine 

* by calling the build_and_run.sh shellscript

e.g.bash build_and_run.sh /PATH/TO/BE/MONITORED mqttbrokeraddress mqttbrokerport

bash build_and_run.sh /home/rkumarv/test mqtt.eclipseprojects.io 1883

This will create a separate docker image and main.py will be executed within the container

### Note : MQTT over unencrypted TCP is utilized in this module

## Contact

* Email: ramkumar2611v@gmail.com
