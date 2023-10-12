"""
This Script monitors a specified file/directory for change events.

In case of Changes, event_type, file/directory type, timestamp of event is published onto a mqtt topic which is
the absolute path to the changed file.

Path to be monitored, MQTT Broker address & port to be defined while calling the function
e.g.  python3 main.py --path=/home/rkumarv/test --address=mqtt.eclipseprojects.io --port=1883
"""
import argparse
import os
import time
from datetime import datetime

import paho.mqtt.client as mqtt
import pyinotify


class EventHandler(pyinotify.ProcessEvent):
    """
    Handler Class to process inotify events
    """
    _methods = [
        "IN_CREATE",
        "IN_OPEN",
        "IN_ACCESS",
        "IN_ATTRIB",
        "IN_CLOSE_NOWRITE",
        "IN_CLOSE_WRITE",
        "IN_DELETE",
        "IN_DELETE_SELF",
        "IN_IGNORED",
        "IN_MODIFY",
        "IN_MOVE_SELF",
        "IN_MOVED_FROM",
        "IN_MOVED_TO",
        "IN_Q_OVERFLOW",
        "IN_UNMOUNT",
        "default",
    ]

    def process_generator(cls, method, mqtt_client, topic):
        def _method_name(self, event):
            """
            Separate process handlers are created for each event specified on _methods
            """
            payload = {}
            payload.update({"event": event.maskname})
            payload.update({"is_directory": event.dir})
            payload.update({"timestamp": datetime.now().isoformat()})
            mqtt_client.publish(topic=topic, payload=str(payload))
            print("published - " + str(payload) + " onto Topic " + topic)
            if event.maskname == "IN_DELETE_SELF":
                time.sleep(1)
                raise NameError(topic + " does not exist anymore...!!!")

        _method_name.__name__ = "process_{}".format(method)
        setattr(cls, _method_name.__name__, _method_name)


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


if __name__ == "__main__":
    root_dir = os.getcwd()
    args = get_arguments(root_dir)
    client = mqtt.Client()
    actual_path = args.path
    a = args.path.split("/docker/host_root", 1)
    if a[0] == "":
        actual_path = a[1]
    try:
        print("Making MQTT Connection")
        client.connect(args.address, int(args.port), 60)
        print("Mqtt Broker Connected Successfully onto", args.address)
        wm = pyinotify.WatchManager()  # Watch Manager
        handler = EventHandler()
        notifier = pyinotify.Notifier(wm, handler)
        wdd = wm.add_watch(args.path, pyinotify.ALL_EVENTS)
        if wdd[args.path] == -1:
            raise NameError("Unable to add watch on " + actual_path)
        else:
            print("New Watch Added onto", actual_path)
        for method in EventHandler._methods:
            EventHandler.process_generator(EventHandler, method, client, actual_path)
        notifier.loop()
    except Exception as e:
        client.disconnect()
        print(e)