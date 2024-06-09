#!/bin/bash

# Install the required Python package
echo -e "\e[1;33minstalling pymongo\e[0m"
pip install pymongo

# Run the Python script to export MongoDB collection to CSV
echo -e "\e[1;33mrunning collection to CSV\e[0m"
python3 collection2csv.py