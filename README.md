# TrackIR
A proof of concept for detecting humans and animals via thermal vision and notifying a user via meshtastic messages

Setup:

1. In config.example.json, enter the destinationId of your Meshtastic that will be receiving notifications. Rename this to config.json
2. Install torch with CUDA with the version needed for your GPU. The CUDA version can be found by running nvidia-smi. For example, with a cuda version of 13.0, the command would be - pip install torch --index-url https://download.pytorch.org/whl/cu130
2. Create a virtual environment and run pip install -r requirements.txt


