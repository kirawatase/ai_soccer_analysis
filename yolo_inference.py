from ultralytics import YOLO
import os

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

# Run prediction
print(f"Running prediction on video: {input_video}")
results = model.predict(input_video, save=True, project=output_dir, name='run1')
print("Prediction completed")

# Check results
if results:
    print(f"Number of frames processed: {len(results)}")
    print(f"First frame results: {results[0]}")
    print('------------------')
    for box in results[0].boxes:
        print(box)
else:
    print("No results returned from prediction")

# Check if output files were created
expected_output = os.path.join(output_dir, 'run1')
if os.path.exists(expected_output):
    print(f"Output folder created: {expected_output}")
    print("Contents:")
    for item in os.listdir(expected_output):
        print(f" - {item}")
else:
    print(f"Output folder not found: {expected_output}")

print("Script execution completed")