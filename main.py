import cv2
import json
from ultralytics import YOLO
from meshtastic_notifier import MeshtasticNotifier

with open("config.json") as f:
            config = json.load(f)

# Load a pretrained YOLO model (downloads automatically on first run)
model = YOLO('yolov8n.pt')
notifier = MeshtasticNotifier()

# Open the test video
print("this is before")
cap = cv2.VideoCapture(config["videoPath"])
print("test")
if not cap.isOpened():
    print("Error: Could not open camera. Please check port settings and try again")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("End of video reached.")
        break

    # Run detection on this frame. Only detect people.
    results = model(frame, classes = [0], verbose=False)

    # If a person was detected, send a notification
    
    if len(results[0].boxes) > 0 and notifier.can_send():
        sent = notifier.notify_person_detected()
        if sent:
            print("Alert sent.")
    

    # Draw bounding boxes, labels, and confidence scores onto the frame
    annotated_frame = results[0].plot()

    # Show it
    cv2.imshow('YOLO Test', annotated_frame)

    # Press 'q' to quit early
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()