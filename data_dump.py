import pymongo
import pandas as pd
import json
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATA_FILE_PATH = "aps_failure_training_set1.csv"
DATABASE_NAME = "aps"
COLLECTION_NAME = "sensor"

if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    # print(f"rows and columns: {df.shape}")
    
    # convert df to json so that we can dump the records into db
    df.reset_index(drop=True,inplace=True)
    json_records = list(json.loads(df.T.to_json()).values()) # this will give the column wise data
    
    # print(json_records[0])

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_records)
