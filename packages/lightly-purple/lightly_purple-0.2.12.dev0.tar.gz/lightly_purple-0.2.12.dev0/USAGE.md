<div align="center">
<p align="center">

<!-- prettier-ignore -->
<img src="https://cdn.prod.website-files.com/62cd5ce03261cba217188442/66dac501a8e9a90495970876_Logo%20dark-short-p-800.png" height="50px">

**The open-source tool curating datasets**

---

[![PyPI python](https://img.shields.io/pypi/pyversions/lightly-purple)](https://pypi.org/project/lightly-purple)
[![PyPI version](https://badge.fury.io/py/fiftyone.svg)](https://pypi.org/project/fiftyone)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

</p>
</div>

# 🚀 Aloha!

We at **[Lightly](https://lightly.ai)** created an open-source tool that supercharges your data curation workflows by enabling you to explore datasets, analyze data quality, and improve your machine learning pipelines more efficiently than ever before. Embark with us in this adventure of building better datasets. .

## 💻 **Installation**

Please use Python 3.8 or higher with venv. Works on Windows, Linux, and macOS.

```shell
# Create virtual environment
# On Linux/macOS:
python3 -m venv venv
source venv/bin/activate

# On Windows:
python -m venv venv
.\venv\Scripts\activate

# Install library
pip install lightly-purple

```

## **Quickstart**

Download the dataset and run a quickstart script to load your dataset and launch the app.

Here are few examples for you to try out:

YOLO8 dataset:

```shell
# Download and extract dataset
export DATASET_PATH=$(pwd)/example-dataset && \
    bash <(curl -sL https://raw.githubusercontent.com/lightly-ai/gists/refs/heads/main/fetch-dataset.sh) \
        https://universe.roboflow.com/ds/nToYP9Q1ix\?key\=pnjUGTjjba \
        $DATASET_PATH

# Download example script
curl -sL https://raw.githubusercontent.com/lightly-ai/gists/refs/heads/main/example-yolo8.py > example.py

# Run the example script
python example.py
```

The YOLO dataset should follow this structure:

```
dataset/
├── train/
│   ├── images/
│   │   ├── image1.jpg
│   │   ├── image2.jpg
│   │   └── ...
│   └── labels/
│       ├── image1.txt
│       ├── image2.txt
│       └── ...
├── valid/  (optional)
│   ├── images/
│   │   └── ...
│   └── labels/
│       └── ...
└── data.yaml
```

Each label file should contain YOLO format annotations (one per line):

```
<class> <x_center> <y_center> <width> <height>
```

Where coordinates are normalized between 0 and 1.

Let's break down what these commands do:

1. **Setting up the dataset path**:

   ```shell
   export DATASET_PATH=$(pwd)/example-dataset
   ```

   This creates an environment variable `DATASET_PATH` pointing to an 'example-dataset' folder in your current directory.

2. **Downloading and extracting the dataset**:

   ```shell
   bash <(curl -sL https://raw.githubusercontent.com/lightly-ai/gists/refs/heads/main/fetch-dataset.sh)
   ```

   - Downloads a shell script that handles dataset fetching
   - The script downloads a YOLO-format dataset from Roboflow
   - Automatically extracts the dataset to your specified `DATASET_PATH`

3. **Getting the example code**:

   ```shell
   curl -sL https://raw.githubusercontent.com/lightly-ai/gists/refs/heads/main/example-yolo8.py > example.py
   ```

   Downloads a Python script that demonstrates how to:

   - Load the YOLO dataset
   - Process the images and annotations
   - Launch the Lightly Purple UI for exploration

4. **Running the example**:
   ```shell
   python example.py
   ```
   Executes the downloaded script, which will:
   - Initialize the dataset processor
   - Load and analyze your data
   - Start a local server
   - Open the UI in your default web browser

## 🔍 **How It Works**

Lightly Purple helps you understand and curate your datasets through several key components:

### Core Components

- **Dataset Processor**: Prepares your data and annotations by:

  - Loading and preprocessing datasets
  - Handling various data formats and annotation types
  - Computing metadata
  - Performing quality analysis

- **Data Storage Layer**: Manages persistent data storage:

  - Stores raw dataset files and annotations
  - Maintains computed metadata
  - Caches processed results for quick access
  - Provides efficient data retrieval interfaces

- **Backend API**: Manages processed data and serves as the information hub:

  - Stores dataset metadata and analysis results
  - Handles data queries and filtering
  - Provides endpoints for dataset exploration
  - Manages user interactions with the data

- **Modern UI Application**: A responsive web interface that:
  - Consumes local API endpoints
  - Visualizes your dataset and analysis results
  - Provides interactive exploration tools
  - Enables dataset curation workflows
