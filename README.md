# TrackIR

A proof of concept for detecting humans via thermal or standard cameras and notifying a user via Meshtastic messages.

## Requirements

1. A Linux device. Windows support is planned and will be coming in the near future
2. Two Meshtastic nodes, with the ability of viewing the node ID of the receiving node
3. A camera to be used for detection. While a thermal optic is intended for use with this program, a standard camera is also compatible

## Setup

1. **Create and activate a Python virtual environment.**

   A virtual environment is a self-contained folder that keeps this project's Python packages separate from the rest of your system, so nothing conflicts with other projects. This application was developed on Python 3.13.

   First, check that Python is installed and confirm its version:
   ```bash
   python3 --version
   ```
   If this returns an error, or a version below 3.13, you'll need to install Python 3.13 before continuing.

   Next, open a terminal in the TrackIR project folder and create the virtual environment. This creates a new folder named `venv` containing a private copy of Python:
   ```bash
   python3 -m venv venv
   ```

   Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```
   You'll know it worked if you see `(venv)` appear at the beginning of your terminal prompt. This means any packages you install next will be installed inside this environment rather than system-wide.

   > **Note:** You'll need to run the activation command again each time you open a new terminal to work on this project. When you're done working, you can type `deactivate` to exit the virtual environment.

2. **Install PyTorch with CUDA support for your GPU.**

   Find your CUDA version by running:
   ```bash
   nvidia-smi
   ```
   Look for the "CUDA Version" listed in the output. Then install the matching PyTorch build. For example, with CUDA 13.0:
   ```bash
   pip install torch --index-url https://download.pytorch.org/whl/cu130
   ```

3. **Install the remaining dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create your configuration file.** Make a copy of `config.example.json` and rename it to `config.json`.

5. **Configure the variables in `config.json`:**

   | Variable | Description |
   |---|---|
   | `destinationId` | The node ID of the Meshtastic node you're sending messages to. |
   | `cooldownSeconds` | After a message is sent, how long the program waits before checking again for a person in frame. |
   | `messagingEnabled` | Enables/disables messaging (disabled by default). Useful for verifying camera and device function before sending real messages. When `false`, output is printed to the console instead. |
   | `serialPortMeshtastic` | The serial port path for your connected Meshtastic node. |
   | `videoPath` | The path to your camera device, or to a video file for testing. |
