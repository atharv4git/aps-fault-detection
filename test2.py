import pymongo
import pandas as pd

client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client['aps']
collection = database['sensor']

# print(client)
# for i in collection.find():
#     print(i)
df = pd.DataFrame(list(collection.find()))
print(df.head())