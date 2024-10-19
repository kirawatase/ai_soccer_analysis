from ultralytics import YOLO
import os
import cv2

# Print current working directory
print(f"Current working directory: {os.getcwd()}")

# Load the model
model = YOLO('models/best.pt')
print("Model loaded successfully")

# Define input and output paths
input_video = 'input_videos/08fd33_4.mp4'
output_dir = os.path.join(os.getcwd(), 'yolo_output')

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)
print(f"Output directory created/verified: {output_dir}")

# Initialize video capture
cap = cv2.VideoCapture(input_video)

# Process video frame by frame
frame_count = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # Stop if there are no more frames
    
    # Run YOLO prediction on the current frame
    results = model(frame)
    
    # Save results for each frame (optional)
    frame_output_path = os.path.join(output_dir, f'frame_{frame_count}.jpg')
    cv2.imwrite(frame_output_path, frame)  # Save the current frame if needed
    
    # Print information about results for the current frame
    if results:
        print(f"Processed frame {frame_count}")
        for box in results[0].boxes:
            print(box)  # Print each bounding box in the frame
    frame_count += 1

cap.release()  # Release the video capture object

# Check if output files were created
if os.path.exists(output_dir):
    print(f"Output folder created: {output_dir}")
    print("Contents:")
    for item in os.listdir(output_dir):
        print(f" - {item}")
else:
    print(f"Output folder not found: {output_dir}")

print("Script execution completed")
