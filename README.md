# Image-Preprocessing
This project involves preprocessing images for computer vision tasks.

## 1. Installation

- Clone the project:
    ```bash
    git clone https://github.com/vantoan2905/Image-Preproces.git
    ```

- You can install Anaconda or Miniconda.

- After installing, you can proceed to install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

## 2. Download Data from Kaggle

To download data from Kaggle, you need to set up the Kaggle API. Follow these steps:

1. Install the `kaggle` package:
    ```bash
    pip install kaggle
    ```

2. Place your `kaggle.json` file (containing your Kaggle API credentials) in the correct directory:
    ```bash
    mkdir ~/.kaggle
    cp /path/to/kaggle.json ~/.kaggle/
    chmod 600 ~/.kaggle/kaggle.json
    ```

3. Download the dataset:
    ```python
    !kaggle datasets download -d davidbroberts/brain-tumor-object-detection-datasets
    ```

## 3. Commit Guidelines

- `feat`: Add a new feature.
- `fix`: Fix a bug.
- `refactor`: Refactor code without changing behavior.
- `test`: Add or fix tests.
- `docs`: Change documentation.
- `style`: Change related to formatting (does not affect logic).
- `chore`: Miscellaneous tasks (configuration, build, etc.).

