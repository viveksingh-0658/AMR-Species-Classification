# ============================================================
# File Name: sample_images_visualization.py
#
# Purpose:
# Display one sample image from different microbial species.
#
# This helps us visually inspect the dataset before training.
# ============================================================

# Import required libraries
import os
from PIL import Image
import matplotlib.pyplot as plt

# Dataset path
dataset_path = "archive"

# Select a few species for visualization
selected_species = [
    "Escherichia.coli",
    "Staphylococcus.aureus",
    "Pseudomonas.aeruginosa",
    "Proteus"
]

# Create figure
plt.figure(figsize=(12, 8))

# Loop through selected species
for index, species in enumerate(selected_species):

    # Create folder path
    species_path = os.path.join(dataset_path, species)

    # Get first image
    image_file = os.listdir(species_path)[0]

    # Create full image path
    image_path = os.path.join(species_path, image_file)

    # Open image
    image = Image.open(image_path)

    # Create subplot
    plt.subplot(2, 2, index + 1)

    # Display image
    plt.imshow(image)

    # Show species name
    plt.title(species)

    # Hide axis
    plt.axis("off")

# Adjust layout
plt.tight_layout()

# Show figure
plt.show()