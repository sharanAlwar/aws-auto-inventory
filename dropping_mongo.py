from pymongo import MongoClient

def delete_all_collections(db_name):
    client = MongoClient("")
    db = client[""]
    
    collections = db.list_collection_names()
    
    for collection in collections:
        db[collection].drop()
        print(f'Dropped collection: {collection}')
    
    client.close()

delete_all_collections('your_database_name')
