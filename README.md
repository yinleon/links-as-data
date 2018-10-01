# Links as Data
Leon Yin 2018-10-01

## Introduction
This  repo contains a Jupyter notebook (view it here on Github, or here on NBViewer) which demos how to extract URLs from Twitter data, preprocess and expand them, and perform rudimentary data analysis using supervised and unsupervied machine learning. The notebook and some auxilliary files are in the `nbs` (short for notebooks) directory. Where `congress-links.ipnb` is the main notebook, `download_data.py` is a script to download the raw and intermediate data used in the notebook, and `config.py` contains gloval variables for where data is stored locally.

## Requirements
This notebook is intended to be run with Python 3.6 or above, utilizing default packages as well as open source packages in `requirements.txt`.

Please download them using:
```pip install -R requirements.txt```

These resources can be run either on NYU HPC, or locally on your personal machine.
You may want to take a look at `config.py` for an idea of where data is coming from and where it wil be sotred. From the nbs directory, run the `python download_data.py` to download the data necessary to run this tutorial.

## Installation
This is a public repository, clone the repo!<br>
If you use the Terminal or another command line client, you can do so with:
```git clone git@github.com:yinleon/links-as-data.git```
In whatever working directory you choose.