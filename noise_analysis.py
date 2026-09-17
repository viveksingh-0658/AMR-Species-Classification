# Import required libraries
import os
import cv2
import numpy as np

# Dataset folder path
dataset_path = "archive"

# List to store noise values of all images
noise_scores = []

# Loop through all species folders
for species in os.listdir(dataset_path):

    species_path = os.path.join(dataset_path, species)

    # Skip if not a folder
    if not os.path.isdir(species_path):
        continue

    # Loop through all images inside the species folder
    for image_name in os.listdir(species_path):

        # Process only .tif images
        if image_name.endswith(".tif"):

            image_path = os.path.join(species_path, image_name)

            try:
                # Read image in grayscale mode
                img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

                # Skip if image could not be read
                if img is None:
                    continue

                # Calculate standard deviation of pixel values
                # Higher value = more variation = more noise
                noise_value = np.std(img)

                # Store noise value
                noise_scores.append(noise_value)

            except Exception:
                continue

# Print final report
print("\nNOISE ANALYSIS REPORT\n")

print("Total Images Checked :", len(noise_scores))
print("Average Noise Score  :", np.mean(noise_scores))
print("Minimum Noise Score  :", np.min(noise_scores))
print("Maximum Noise Score  :", np.max(noise_scores))