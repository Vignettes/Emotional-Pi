import cv2
from fer import FER

# Initialize the camera
cap = cv2.VideoCapture(0, cv2.CAP_V4L2)

# Set frame dimensions (optional for performance)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Initialize the emotion detector
detector = FER(mtcnn=True)  # Using MTCNN for face detection

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Detect emotions in the frame
    results = detector.detect_emotions(frame)

    # Iterate over detected faces
    for result in results:
        # Get bounding box
        (x, y, w, h) = result["box"]

        # Draw rectangle around face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Get emotion with highest score
        emotions = result["emotions"]
        max_emotion = max(emotions, key=emotions.get)
        confidence = emotions[max_emotion]

        # Put text above rectangle
        cv2.putText(frame, f"{max_emotion} ({confidence:.2f})", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Emotion Detection', frame)

    # Exit condition
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

