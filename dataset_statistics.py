import os

# Dataset folder path
dataset_path = "archive"

# Total classes (species) count
total_classes = 0

# Total images count
total_images = 0

# Store smallest class information
smallest_class = ""
smallest_count = float('inf')

# Store largest class information
largest_class = ""
largest_count = 0

print("\nCLASS DISTRIBUTION\n")

# Loop through all folders inside archive
for folder in sorted(os.listdir(dataset_path)):

    # Create full path of current folder
    folder_path = os.path.join(dataset_path, folder)

    # Check if current item is a directory
    if os.path.isdir(folder_path):

        # Count images recursively (handles nested folders)
        image_count = 0

        for root, dirs, files in os.walk(folder_path):

            # Count only .tif image files
            image_count += len(
                [file for file in files if file.endswith(".tif")]
            )

        # Increase class count
        total_classes += 1

        # Add images to total image count
        total_images += image_count

        # Print current class and image count
        print(f"{folder} : {image_count}")

        # Check for smallest class
        if image_count < smallest_count:
            smallest_count = image_count
            smallest_class = folder

        # Check for largest class
        if image_count > largest_count:
            largest_count = image_count
            largest_class = folder

# Print final dataset statistics
print("\n------------------------------")
print("Total Classes :", total_classes)
print("Total Images  :", total_images)
print("------------------------------")
print("Smallest Class :", smallest_class, "-", smallest_count)
print("Largest Class  :", largest_class, "-", largest_count)