import os
import csv
import pytesseract
from PIL import Image

# Path to the image folder
image_folder = "images-ocr"

# Path to the CSV file to store OCR results
csv_file = os.path.join(image_folder, f"{os.path.basename(image_folder)}.csv")

# Confidence threshold for ignoring OCR results
confidence_threshold = 1
print(confidence_threshold)

# Set the page segmentation mode to PSM_SINGLE_BLOCK
custom_config = r'--psm 11'

# Initialize an empty list to store OCR results
ocr_results = []

# Initialize counters for the number of characters and total confidence scores
total_chars = 0
total_confidence = 0

# Loop through all the image files in the folder
for filename in os.listdir(image_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        print("processing image ",filename)
        # Load the image
        image_path = os.path.join(image_folder, filename)
        image = Image.open(image_path)
        
        # Perform OCR on the image using Pytesseract
        ocr_data = pytesseract.image_to_data(image, output_type='dict', config=custom_config)
        
        # Extract the OCR result and confidence scores for characters above the threshold
        ocr_chars = [word for word, confidence in zip(ocr_data['text'], ocr_data['conf']) if confidence >= confidence_threshold]
        ocr_confidences = [confidence for confidence in ocr_data['conf'] if confidence >= confidence_threshold]
        
        # Calculate the average confidence score for characters above the threshold
        avg_confidence = sum(ocr_confidences) / len(ocr_confidences) if len(ocr_confidences) > 0 else 0
        
        # Append the OCR result and average confidence level to the list
        ocr_results.append((filename, ' '.join(ocr_chars), avg_confidence))
        
        # Update the counters for the number of characters and total confidence scores
        total_chars += len(ocr_chars)
        total_confidence += sum(ocr_confidences)
        print(ocr_chars)
        print(total_confidence)
        print("")

# Calculate the overall average confidence score for characters above the threshold
overall_avg_confidence = total_confidence / total_chars if total_chars > 0 else 0

# Write the OCR results to a CSV file
with open(csv_file, mode="w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["filename", "ocr_text", "avg_confidence"])
    writer.writerows(ocr_results)

# Print the overall average confidence score
print(f"Overall average confidence score: {overall_avg_confidence}")
