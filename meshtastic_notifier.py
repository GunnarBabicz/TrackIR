import json
import meshtastic
import meshtastic.serial_interface

with open("config.json") as f:
    config = json.load(f)

interface = meshtastic.serial_interface.SerialInterface()
interface.sendText("testing API", destinationId=config["destinationId"])