import pandas as pd
from sensor.config import mongo_client
from sensor.exception import SensorException
from sensor.logger import logging
import sys,os

def get_collections_as_dataframe(database_name:str, collection_name:str)->pd.DataFrame:

    """
    Description: this function returns collection as dataframe
    database_name = database name
    collection_name = collectin name
    =================================================
    return Pandas dataframe of a collection
    """

    try:
        logging.info(f"Reading data from database: {database_name} and collection: {collection_name}")
        df = pd.DataFrame(list(mongo_client[database_name][collection_name].find()))
        logging.info(f"found columns: {df.columns}")
        logging.info(f"Dropping column: _id ")
        if "_id" in df.columns:
            df = df.drop("_id", axis=1)
    except Exception as e:
        raise SensorException(e, sys)