# TrackIR
A proof of concept for detecting humans via thermal or standard cameras and notifying a user via meshtastic messages

# Setup:

1. Create a Python virtual environment in this folder and activate it (developed on version 3.13)
2. Install torch with CUDA with the version needed for your GPU. The CUDA version can be found by running nvidia-smi. For example, with a cuda version of 13.0, the command would be - pip install torch --index-url https://download.pytorch.org/whl/cu130
3. install the dependencies needed for the environment: pip install -r requirements.txt
4. Create a copy of config.example.json and rename this "config.json"
5. Configure the variables in config.json for the program. Below is an explanation of each value:

  "destinationId" - This will be the node ID for the meshtastic node that you are sending your message to
  "cooldownSeconds" - One a message is sent, the program will wait this long until checking again if there is a person in frame
  "messagingEnabled" - This can be used to disable messaging (as is selected by default). Useful for ensuring camera and device function before attempting to send messages. When set to false, this will print to the console.
  "serialPortMeshtastic" - This will need to be configured to the path of the serial port your Meshtastic node is connected to
  "videoPath" - This will need to be configured to the path of your camera, or to the path of a video if this is being used for testing


