Filesystem Change Monitor with MQTT Publishing



Requirements:

1. Command-line Interface:

    - The module should accept command-line arguments:

        - `--path`, indicating which directory or file to monitor,

        - `--address`, indicating the MQTT broker address,

        - `--port`, indicating the MQTT broker port.

    - Example: `python monitor.py --path /path/to/directory --address 127.0.0.1 --port 1883`

2. Filesystem Monitoring:

    - Monitor the specified directory or file for any write/modify etc. events.

    - Utilize appropriate libraries like `inotify` to achieve this.

3. MQTT Integration:

    - When a change is detected, publish an MQTT message.

    - The topic should be the absolute path to the changed file.

    - Determine the message payload to best represent the change event. Be ready to justify your choice.

4. Docker Integration:

   - Provide a `Dockerfile` that creates an environment for running the module.

    - This should include all necessary dependencies.

    - Ensure the `Dockerfile` sets up the necessary command to run the module when the container starts.

5. Documentation:

    - Provide a `README.md` that contains:

        - A brief overview of the project.

        - Instructions on how to build the Docker image.

        - Instructions on how to run the Docker container with necessary parameters (like path to monitor).

        - Any other relevant details or explanations that might help in understanding or using the tool.



Hints:

- Consider using the `paho-mqtt` Python library for MQTT communication.

- Think about how the module might handle large files or rapid sequences of changes.

- Handle edge cases gracefully, such as trying to monitor a non-existent path or facing permission issues.

