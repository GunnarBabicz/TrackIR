import json
import time
from datetime import datetime

import meshtastic
import meshtastic.serial_interface


class MeshtasticNotifier:
    def __init__(self, config_path="config.json"):
        with open(config_path) as f:
            config = json.load(f)

        self.destination_id = config["destinationId"]
        self.cooldown_seconds = config["cooldownSeconds"]
        self.enabled = config["messagingEnabled"]
        self.last_sent_time = 0

        self.interface = None
        if self.enabled:
            self.interface = meshtastic.serial_interface.SerialInterface(devPath = config["serialPortMeshtastic"])

    def can_send(self):
        return time.time() - self.last_sent_time >= self.cooldown_seconds

    def notify_person_detected(self):
        if not self.can_send():
            return False

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = (
            f"PERSON DETECTED AT {timestamp}. "
            f"WILL REACCESS IN {self.cooldown_seconds} SECONDS."
        )

        if self.enabled:
            self.interface.sendText(message, destinationId=self.destination_id)
        else:
            print(f"DRY RUN. Would send: {message}")
        
        self.last_sent_time = time.time()
        return True