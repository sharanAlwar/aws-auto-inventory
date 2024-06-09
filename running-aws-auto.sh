#!/bin/bash

# Update package lists
echo -e "\e[1;33mUpdating package lists...\e[0m"
sudo apt update

# Upgrade all installed packages to their latest versions
echo -e "\e[1;33mUpgrading installed packages...\e[0m"
sudo apt upgrade -y

# Install AWS CLI
echo -e "\e[1;33mInstalling AWS CLI...\e[0m"
sudo apt install -y awscli

# Set AWS credentials and default region
echo -e "\e[1;33mConfiguring AWS CLI...\e[0m"
export AWS_ACCESS_KEY_ID=""
export AWS_SECRET_ACCESS_KEY=""
export AWS_DEFAULT_REGION="us-east-1"

# Install Python 3 and pip
echo -e "\e[1;33mInstalling Python 3 and pip...\e[0m"
sudo apt install -y python3-pip

# Install required Python packages
echo -e "\e[1;33mInstalling Python packages...(boto3 & pymongo)\e[0m"
pip install boto
pip install boto3
pip install pymongo

# Execute the Python script
echo -e "\e[1;33mrunning aws-inventory.py\e[0m"
python3 aws-inventory.py