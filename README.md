# Asset Prices


This repository contains a python program that create a plots on a variety of aspects using the MX Nordic 40 stock market index. 

## 📁 Project Structure

```

├── mainCode.py
├── unitTest.py
├── requirements.txt
├── historicalData.csv
├── LICENSE
└── README.md
└── .circle.ci/
    └── config.yml

```

## 📊 Dataset

The dataset used was obtained from Nasdaq:
1. [MX Nordic 40 (OMXN40) Historical Data](https://www.nasdaq.com/market-activity/index/omxn40/historical?page=25&rows_per_page=10&timeline=y1)
    * Data downloaded for the year 2025 on 20/10/2025


## 🛠️ Installation

Python 3.10 or newer to run python files

Python modules required:

* pandas – reading and handling CSV files.
* matplotlib – plotting graphs.
* os - checking if files exist.
* tempfile - to unit test csv

You can install required packages with:

```
pip install pandas matplotlib os tempfile

```


## 📄 License
This project is open source and available under the [MIT License](https://github.com/hafybufya/asset-prices/blob/main/LICENSE).
