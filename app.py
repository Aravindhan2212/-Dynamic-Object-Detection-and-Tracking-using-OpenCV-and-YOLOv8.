import streamlit as st #pip install streamlit
import cv2 #pip install opencv-python
import numpy as np
from ultralytics import YOLO #pip install  ultralytics
import tempfile
import os

# Load the pre-trained YOLOv8 model
model = YOLO("yolov8n.pt")  # Ensure the model file is in the same directory or provide the correct path

# Streamlit app title
st.title("Real-Time Object Detection with YOLOv8")

# Input source selection
source_option = st.sidebar.radio("Select Source", ["Upload Video", "Upload Image", "Use Webcam"])

# Initialize video capture variable
video_capture = None

if source_option == "Upload Video":
    uploaded_file = st.file_uploader("Choose a video...", type=["mp4", "mov", "avi"])
    if uploaded_file is not None:
        # Save the uploaded file to a temporary file
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_file.read())
        video_capture = cv2.VideoCapture(tfile.name)

elif source_option == "Upload Image":
    uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_image is not None:
        # Read the image file
        image = np.array(bytearray(uploaded_image.read()), dtype=np.uint8)
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)

        # Perform object detection
        results = model(image)

        # Draw bounding boxes on the image
        for result in results:
            boxes = result.boxes
            for box in boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])  # Get bounding box coordinates
                conf = box.conf[0]  # Get confidence score
                label = f"{model.names[int(box.cls[0])]}: {conf:.2f}"  # Get label and confidence
                cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)  # Draw rectangle
                cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        # Display the annotated image
        st.image(image, channels="BGR", use_container_width=True)

else:
    video_capture = cv2.VideoCapture(0)  # Use webcam

# Process video frames if video is selected
if video_capture is not None and video_capture.isOpened():
    # Create a temporary directory to save the output video
    output_video_path = tempfile.NamedTemporaryFile(delete=False, suffix=".avi").name
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    
    # Get the width and height of the video
    width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    # Create a VideoWriter object
    out = cv2.VideoWriter(output_video_path, fourcc, 30.0, (width, height))

    # Set the maximum number of frames to process
    max_frames = 50
    frame_count = 0

    while frame_count < max_frames:
        ret, frame = video_capture.read()
        if not ret:
            st.write("No more frames to read.")
            break

        # Perform object detection
        results = model(frame)

        # Draw bounding boxes on the frame
        for result in results:
            boxes = result.boxes
            for box in boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])  # Get bounding box coordinates
                conf = box.conf[0]  # Get confidence score
                label = f"{model.names[int(box.cls[0])]}: {conf:.2f}"  # Get label and confidence
                cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)  # Draw rectangle
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        # Write the annotated frame to the output video
        out.write(frame)

        # Display the annotated frame in the Streamlit app
        st.image(frame, channels="BGR", use_container_width=True)

        # Increment the frame counter
        frame_count += 1

    # Release the video capture and writer objects
    video_capture.release()
    out.release()

    # Provide a download link for the output video
    with open(output_video_path, "rb") as f:
        st.download_button("Download Processed Video", f, file_name="output_video.avi")

    # Clean up temporary files
    os.remove(output_video_path)