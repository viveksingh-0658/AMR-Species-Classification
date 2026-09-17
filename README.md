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
- Dataset Visualization
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

## Stage 2: Data Exploration (Completed)

### Tasks Performed

- Dataset structure verification
- Random image inspection
- Image resolution check
- RGB / Grayscale verification
- Class distribution analysis
- Corrupted image detection
- Blur analysis
- Noise analysis

### Dataset Statistics

- Total Classes: 33
- Total Images: 692
- Resolution: 2048 × 1532
- Color Mode: RGB
- Corrupted Images: 3

### Image Quality Analysis

#### Blur Analysis

- Average Blur Score: 22.54
- Minimum Blur Score: 6.52
- Maximum Blur Score: 97.61

#### Noise Analysis

- Average Noise Score: 26.62
- Minimum Noise Score: 5.80
- Maximum Noise Score: 65.77

### Conclusion

The dataset is suitable for deep learning based microbial image classification.

## Extra Notes in stage 2 
### Image Resolution Check(file name image_resoluction_cheak.py)

- Verified image dimensions across dataset
- Resolution found: 2048 × 1532 pixels
- Detected and removed 3 corrupted TIFF images
- Dataset cleaned before preprocessing

### Blur Analysis Observation (blur_analysis.py)

Blur analysis was performed using the Variance of Laplacian method.

A total of 669 images were successfully analyzed.

- Average Blur Score: 22.54
- Minimum Blur Score: 6.52
- Maximum Blur Score: 97.61

The results indicate that most images contain sufficient edge information and are suitable for feature extraction and CNN-based image classification. A few images show lower sharpness but no severe blur issues were observed across the dataset.

## Noise Analysis(python_noise_analysis.py)

Noise analysis was performed using the standard deviation of pixel intensities.

Results:

- Total Images Checked: 669
- Average Noise Score: 26.62
- Minimum Noise Score: 5.80
- Maximum Noise Score: 65.77

Observation:

The dataset exhibits moderate pixel intensity variation. The images are suitable for machine learning and deep learning based image classification tasks.


### Stage 3: Dataset Visualization
Goal
Dataset ko visually understand karna.
## Stage 3 Progress

### Dataset Visualization

- Created class distribution visualization
- Generated horizontal bar chart
- Saved visualization in results folder



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