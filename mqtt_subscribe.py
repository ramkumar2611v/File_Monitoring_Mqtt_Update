"""
Script will simply subscribe to a specified topic and listens to the messages
"""

import argparse
import os

import paho.mqtt.client as mqtt


def get_arguments(root_dir):
    """
    Arguments parser to receive command line arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--path", help="path of directory or file to monitor", default=None
    )
    parser.add_argument(
        "--address",
        help="MQTT broker address",
    )
    parser.add_argument(
        "--port",
        help="MQTT broker port",
    )
    return parser.parse_args()


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(args.path)


def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


root_dir = os.getcwd()
args = get_arguments(root_dir)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(args.address, int(args.port), 60)
client.loop_forever()
