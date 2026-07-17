# This outputs a list of the yolo classes to be able to filter what the model needs

import cv2
from ultralytics import YOLO

model = YOLO('yolov8n.pt')

with open('class_names.txt', 'w') as f:
    for class_id, class_name in model.names.items():
        f.write(f"{class_id}: {class_name}\n")