# AMR-Species-Classification
CNN based microbial species classification using microscopy images.


# AMR Species Classification Using Deep Learning

## Project Overview

This project focuses on identifying microbial species from microscopy images using Computer Vision and Deep Learning techniques.

The long-term goal is to build an AI-assisted pipeline that can support Antimicrobial Resistance (AMR) research by automatically recognizing microbial species from microscopic images.

---

## Objectives

- Classify microbial species from microscopy images.
- Explore image-based approaches for microbiology.
- Build a CNN-based classification model.
- Create a foundation for future AMR prediction research.

---

## Dataset

Dataset Used: DIBaS (Digital Image Database for Bacterial Species)

Dataset Characteristics:

- Total Classes: 33
- Total Images: 692
- Image Format: TIFF (.tif)
- Image Resolution: 2048 × 1532
- Color Mode: RGB

The dataset contains microscopy images of different bacterial species and related microorganisms.

---

## Project Roadmap

### Phase 1: Species Classification

- Dataset Collection
- Dataset Exploration
- Image Preprocessing
- Data Augmentation
- CNN Model Development
- Model Evaluation

### Phase 2: AMR Research Extension

- Literature Review
- AMR Dataset Collection
- Species-AMR Mapping
- Resistance Prediction Experiments

---

## Project Structure

```text
AMR_PROJECT/
│
├── archive/                    # Dataset
├── image_exploration.py
├── dataset_statistics.py
├── README.md
├── .gitignore
└── venv/
```

---

## Progress Log

### Week 1

### Stage 1: Dataset Collection ✅

Completed:

- Downloaded DIBaS dataset
- Verified dataset structure
- Verified class folders
- Verified image availability

Results:

- 33 Classes
- 692 Images

---

### Stage 2: Dataset Exploration & Validation ✅

Completed:

- Installed required libraries
- Created Python virtual environment
- Opened TIFF images using Pillow
- Verified image dimensions
- Verified RGB color format
- Examined sample images from multiple classes
- Generated class distribution statistics

Results:

| Property | Value |
|-----------|---------|
| Classes | 33 |
| Images | 692 |
| Format | TIFF |
| Resolution | 2048 × 1532 |
| Color Mode | RGB |

Observations:

- Dataset is nearly balanced.
- Class sizes range between 20–23 images.
- Images are suitable for CNN-based classification.
- High-resolution microscopy images are available.

---

## Technologies Used

### Programming Language

- Python

### Libraries

- Pillow
- OpenCV
- NumPy
- Matplotlib
- Jupyter Notebook

### Future Libraries

- TensorFlow
- Keras
- Scikit-Learn

---

## Current Status

Completed:

- Dataset Collection
- Dataset Exploration

Next Step:

- Image Preprocessing

---

## Author

Vivek Singh

B.Tech Computer Science & Engineering

Galgotias University

GitHub:
https://github.com/viveksingh-0658