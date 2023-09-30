import cv2
import face_recognition

# Load the pre-trained Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load a sample image and convert it to RGB format (required by face_recognition)
image_path = 'path_to_image.jpg'
image = cv2.imread(image_path)
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Detect faces in the image using Haar cascade
faces = face_cascade.detectMultiScale(rgb_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Load pre-trained face recognition models
known_face_encodings = []
known_face_names = []

# Define known faces and their names
known_face_encodings.append(face_recognition.face_encodings(rgb_image)[0])
known_face_names.append("Person 1")

# Loop through the detected faces
for (x, y, w, h) in faces:
    # Crop the face region from the image
    face_image = rgb_image[y:y+h, x:x+w]

    # Recognize the face
    face_encodings = face_recognition.face_encodings(face_image)
    if len(face_encodings) > 0:
        match = face_recognition.compare_faces(known_face_encodings, face_encodings[0])
        name = "Unknown"

        if any(match):
            matched_index = match.index(True)
            name = known_face_names[matched_index]

        # Draw a rectangle and label on the image
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(image, name, (x + 6, y - 6), font, 0.5, (255, 255, 255), 1)

# Display the image with faces detected and recognized
cv2.imshow('Face Detection and Recognition', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
