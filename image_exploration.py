# from PIL import Image

# img = Image.open("/Users/viveksingh/AMR_PROJECT/archive/Escherichia.coli/Escherichia.coli_0001.tif")

# print("Size:", img.size)
# print("Mode:", img.mode)

# from PIL import Image
# import os

# folders = [
#     "Escherichia.coli",
#     "Staphylococcus.aureus",
#     "Pseudomonas.aeruginosa"
# ]

# for folder in folders:
#     file = os.listdir(folder)[0]

#     path = os.path.join(folder, file)

#     img = Image.open(path)

#     print(folder)
#     print("Size:", img.size)
#     print("Mode:", img.mode)
#     print("-" * 30)


# from PIL import Image
# import os

# folders = [
#     "Escherichia.coli",
#     "Staphylococcus.aureus",
#     "Pseudomonas.aeruginosa"
# ]

# base_path = "archive"

# for folder in folders:

#     folder_path = os.path.join(base_path, folder)

#     file = os.listdir(folder_path)[0]

#     path = os.path.join(folder_path, file)

#     img = Image.open(path)

#     print(folder)
#     print("Size:", img.size)
#     print("Mode:", img.mode)
#     print("-" * 30)


from PIL import Image
import os

folders = [
    "Escherichia.coli",
    "Staphylococcus.aureus",
    "Pseudomonas.aeruginosa"
]

base_path = "archive"

for folder in folders:
    try:
        folder_path = os.path.join(base_path, folder)

        file = os.listdir(folder_path)[0]

        path = os.path.join(folder_path, file)

        img = Image.open(path)

        print(folder)
        print("Size:", img.size)
        print("Mode:", img.mode)
        print("-" * 30)

    except Exception as e:
        print("Error in:", folder)
        print(e)