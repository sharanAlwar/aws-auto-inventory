#!/bin/bash

# Update package lists
echo "Updating package lists..."
sudo apt update

# Upgrade all installed packages to their latest versions
echo "Upgrading installed packages..."
sudo apt upgrade -y

# Install AWS CLI
echo "Installing AWS CLI..."
sudo apt install -y awscli

# Set AWS credentials and default region
echo "Configuring AWS CLI..."
export AWS_ACCESS_KEY_ID=""
export AWS_SECRET_ACCESS_KEY=""
export AWS_DEFAULT_REGION="us-east-1"

# Install Python 3 and pip
echo "Installing Python 3 and pip..."
sudo apt install -y python3-pip

# Install required Python packages
echo "Installing Python packages..."
pip install boto3
pip install pymongo

# Execute the Python script
echo "Executing Python script..."
python3 aws-inventory.py

echo "Script completed successfully."
