# simple-tesseract-ocr
Python script that performs Optical Character Recognition (OCR) on images using the Tesseract OCR engine. The script processes all the image files (with the extensions .jpg or .png) present in the specified image folder. It then extracts the OCR results, confidence scores, and calculates average confidence scores for characters above a given confidence threshold. The OCR results are stored in a CSV file, and the overall average confidence score for all the characters above the threshold is printed.

## Requirements
Python libraries `os`, `csv`, `pytesseract`, and `PIL`
Tesseract OCR on your system, as `pytesseract` is just a Python wrapper around the Tesseract OCR engine.


## Code break down:

1. The script imports necessary libraries and modules: `os` for file operations, `csv` for CSV file handling, `pytesseract` for performing OCR, and `PIL` (Python Imaging Library) for image processing.

2. The `image_folder` variable specifies the path to the folder where the images are stored.

3. The `csv_file` variable specifies the path to the CSV file where the OCR results will be saved. The file will be named after the base name of the image folder with a ".csv" extension.

4. The `confidence_threshold` variable is set to 1. This value represents the minimum confidence score needed for the OCR results to be considered valid.

5. The `custom_config` variable is set to `'--psm 11'`, which sets the page segmentation mode to PSM_SINGLE_BLOCK. This mode is used for detecting a single block of text in the image.

6. An empty list `ocr_results` is initialized to store the OCR results for each image.

7. Two counters, `total_chars` and `total_confidence`, are initialized to keep track of the number of characters processed and the total confidence scores, respectively.

8. The script loops through all the files in the image folder and processes only those with ".jpg" or ".png" extensions.

9. For each image, the script loads the image using `PIL.Image.open()`, performs OCR using `pytesseract.image_to_data()` with the custom configuration, and extracts the OCR text and confidence scores for characters above the confidence threshold.

10. The script calculates the average confidence score for the characters above the threshold.

11. The OCR result, average confidence, and filename are appended as a tuple to the `ocr_results` list.

12. The script updates the `total_chars` and `total_confidence` counters with the processed characters and confidence scores for the current image.

13. After processing all the images, the script calculates the overall average confidence score for characters above the threshold using the `total_confidence` and `total_chars` counters.

14. The OCR results are written to the CSV file with the header "filename", "ocr_text", and "avg_confidence".

15. Finally, the overall average confidence score is printed.
