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

Please use Python 3.8 or higher with venv.

```shell
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

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
