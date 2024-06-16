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

# Install Python 3 and pip
echo -e "\e[1;33mInstalling Python 3 and pip...\e[0m"
sudo apt install -y python3-pip

# Install required Python packages
echo -e "\e[1;33mInstalling Python packages...(boto3 & pymongo)\e[0m"
pip install boto
pip install boto3
pip install pymongo

# Set AWS credentials and default region
echo -e "\e[1;33mConfiguring AWS CLI...\e[0m"
export AWS_ACCESS_KEY_ID=""
export AWS_SECRET_ACCESS_KEY=""

# List of AWS regions
regions=("us-east-1" "us-west-1" "us-west-1" "eu-west-1" "eu-west-2" "ap-south-1")

# Loop through each region and execute the commands
for region in "${regions[@]}"
do
    echo -e "\e[1;33m\e[1m\e[3m\e[4mLoading missile for $region\e[0m"
    export AWS_DEFAULT_REGION="$region"

    echo -e "\e[1;31m\e[1m\e[3m\e[4mTargeting $region\e[0m"
    python3 aws-inventory.py
    echo -e "\e[1;32m\e[1m\e[3m\e[4mDestroyed $region\e[0m"
done