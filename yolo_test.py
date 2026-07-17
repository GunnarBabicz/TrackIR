import cv2
from ultralytics import YOLO

# Load a pretrained YOLO model (downloads automatically on first run)
model = YOLO('yolov8n.pt')

# Open the test video
cap = cv2.VideoCapture('videos/test_inside.mp4')

if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("End of video reached.")
        break

    # Run detection on this frame
    results = model(frame, verbose=False)

    # Draw bounding boxes, labels, and confidence scores onto the frame
    annotated_frame = results[0].plot()

    # Show it
    cv2.imshow('YOLO Test', annotated_frame)

    # Press 'q' to quit early
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()