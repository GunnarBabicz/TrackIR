# TrackIR

A proof of concept for detecting humans via thermal or standard cameras and notifying a user via Meshtastic messages.

## Setup

1. Create a Python virtual environment in this folder and activate it (developed on Python 3.13).

2. Install PyTorch with CUDA support for your GPU. Find your CUDA version by running:
   ```bash
   nvidia-smi
   ```
   Then install the matching PyTorch build. For example, with CUDA 13.0:
   ```bash
   pip install torch --index-url https://download.pytorch.org/whl/cu130
   ```

3. Install the remaining dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a copy of `config.example.json` and rename it to `config.json`.

5. Configure the variables in `config.json`:

   | Variable | Description |
   |---|---|
   | `destinationId` | The node ID of the Meshtastic node you're sending messages to. |
   | `cooldownSeconds` | After a message is sent, how long the program waits before checking again for a person in frame. |
   | `messagingEnabled` | Enables/disables messaging (disabled by default). Useful for verifying camera and device function before sending real messages. When `false`, output is printed to the console instead. |
   | `serialPortMeshtastic` | The serial port path for your connected Meshtastic node. |
   | `videoPath` | The path to your camera device, or to a video file for testing. |
