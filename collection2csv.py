from pymongo import MongoClient
import csv

# Connect to the MongoDB database
client = MongoClient("")

# Get the database
db = client[""]

# List of collections to download
collections = ['EC2_Instances', 'Elastic_Blockstore', 'IAM_Users']

# Iterate through the collections
for collection_name in collections:
    # Get the collection
    collection = db[collection_name]

    # Get all the data from the collection
    data = list(collection.find())

    # Create a CSV file
    with open(f'{collection_name}.csv', 'w', newline='') as f:
        # Create a CSV writer object
        writer = csv.writer(f)

        # Write the header row
        writer.writerow(data[0].keys())

        # Write the data rows
        for row in data:
            writer.writerow(row.values())

# Print a success message
print('MongoDB data successfully converted to CSV.')