# ==========================================================
# Blur Analysis for AMR Species Dataset
# Purpose:
# Check whether images are sharp or blurry.
#
# Method:
# Variance of Laplacian
#
# Interpretation:
# Higher value  -> Sharper image
# Lower value   -> Blurrier image
# ==========================================================

# Import required libraries
import os
import cv2
import numpy as np

# Path of the dataset folder
dataset_path = "archive"

# List to store blur scores of all images
blur_scores = []

# Loop through every species folder inside dataset
for species in os.listdir(dataset_path):

    # Create complete path of species folder
    species_path = os.path.join(dataset_path, species)

    # Check whether it is actually a folder
    if os.path.isdir(species_path):

        # Loop through all images of current species
        for image_name in os.listdir(species_path):

            # Create full image path
            image_path = os.path.join(
                species_path,
                image_name
            )

            try:

                # Read image using OpenCV
                img = cv2.imread(image_path)

                # Skip image if OpenCV fails to read it
                if img is None:
                    continue

                # Convert RGB image into grayscale
                # Blur detection works better on grayscale images
                gray = cv2.cvtColor(
                    img,
                    cv2.COLOR_BGR2GRAY
                )

                # Apply Laplacian operator
                # It highlights edges present in the image
                laplacian = cv2.Laplacian(
                    gray,
                    cv2.CV_64F
                )

                # Calculate variance of Laplacian
                # High variance = many edges = sharp image
                # Low variance  = fewer edges = blurry image
                blur_value = laplacian.var()

                # Store blur score
                blur_scores.append(blur_value)

            except Exception as e:

                # Skip corrupted images
                print(
                    f"Error reading {image_path}"
                )

                continue

# ==========================================================
# Final Dataset Blur Statistics
# ==========================================================

print("\nBLUR ANALYSIS REPORT\n")

print(
    "Total Images Checked :",
    len(blur_scores)
)

print(
    "Average Blur Score   :",
    np.mean(blur_scores)
)

print(
    "Minimum Blur Score   :",
    np.min(blur_scores)
)

print(
    "Maximum Blur Score   :",
    np.max(blur_scores)
)