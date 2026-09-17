# PIL library image open karne ke liye
# from PIL import Image

# Operating system ke files/folders access karne ke liye
# import os

# # Dataset ka main folder
# dataset_path = "archive"

# # Unique image sizes store karne ke liye set
# # Set duplicate values store nahi karta
# sizes = set()

# # Archive folder ke andar sabhi species folders par loop
# for species in os.listdir(dataset_path):

#     # Species folder ka complete path
#     species_path = os.path.join(dataset_path, species)

#     # Check karo ki ye folder hai ya nahi
#     if os.path.isdir(species_path):

#         # Folder ke andar aur subfolders ke andar search karo
#         for root, dirs, files in os.walk(species_path):

#             # Har file par loop
#             for file in files:

#                 # Sirf .tif images process karo
#                 if file.endswith(".tif"):

#                     # Complete image path banao
#                     image_path = os.path.join(root, file)

#                     # Image open karo
#                     img = Image.open(image_path)

#                     # Image ka size set me add karo
#                     sizes.add(img.size)

# # Final result print karo
# print("Unique Image Sizes Found:")
# print(sizes)

# ==========================
# Import Libraries
# ==========================

from PIL import Image
import os

# ==========================
# Dataset Path
# ==========================

dataset_path = "archive"

# Unique image sizes store karne ke liye
sizes = set()

# Corrupted images track karne ke liye
corrupted_images = []

# ==========================
# Processing Logic
# ==========================

for species in os.listdir(dataset_path):

    species_path = os.path.join(dataset_path, species)

    if os.path.isdir(species_path):

        for root, dirs, files in os.walk(species_path):

            for file in files:

                if file.endswith(".tif"):

                    image_path = os.path.join(root, file)

                    try:
                        # Image open karo
                        img = Image.open(image_path)

                        # Image size save karo
                        sizes.add(img.size)

                    except Exception:
                        # Agar image open nahi hui
                        corrupted_images.append(image_path)

# ==========================
# Output
# ==========================

print("Unique Image Sizes Found:")
print(sizes)

print("\nCorrupted Images:")

for image in corrupted_images:
    print(image)

print("\nTotal Corrupted Images:", len(corrupted_images))