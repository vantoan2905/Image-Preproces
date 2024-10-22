# Image-Resizing

## 1. Preprocessing Methods for Image Resizing in Deep Learning
- Aspect Ratio Preserving Resize (ARPR)
- Direct Resize (DR)
- Center Crop (CC)
- Random Crop (RC)
- Padding then Resize (PTR)

## 2. Interpolation Methods
- Nearest Neighbor(NN)
- Bilinear Interpolation(BI-Linear)
- Bicubic Interpolation(BI-Cubic)
- Lanczos Resampling(LR)

## 3. Installation

- Clone the project:
    ```bash
    git clone https://github.com/vantoan2905/Image-Preproces.git
    cd Image-Preproces/process_img_resizing
    ```

- You can install Anaconda or Miniconda.

- After installing, you can proceed to install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

- Prepare your data before running the script.

- To run the script, use the following commands:

### Aspect Ratio Preserving Resize (ARPR)
    ```bash
    python main.py path/to/your/image.*** mode=ARPR
    ```

### Direct Resize (DR)
    ```bash
    python main.py path/to/your/image.*** mode=DR
    ```

### Center Crop (CC)
    ```bash
    python main.py path/to/your/image.*** mode=CC
    ```

### Random Crop (RC)
    ```bash
    python main.py path/to/your/image.*** mode=RC
    ```

### Padding then Resize (PTR)
    ```bash
    python main.py path/to/your/image.*** mode=PTR
    ```

### Nearest Neighbor (NN)
    ```bash
    python main.py path/to/your/image.*** mode=NN
    ```

### Bilinear Interpolation (BI-Linear)
    ```bash
    python main.py path/to/your/image.*** mode=BI-Linear
    ```

### Bicubic Interpolation (BI-Cubic)
    ```bash
    python main.py path/to/your/image.*** mode=BI-Cubic
    ```

### Lanczos Resampling (LR)
    ```bash
    python main.py path/to/your/image.*** mode=LR
    ```

