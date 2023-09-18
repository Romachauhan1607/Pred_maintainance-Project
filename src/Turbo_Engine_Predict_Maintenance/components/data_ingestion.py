# data_ingestion.py

import os
import sys
import pandas as pd
from dataclasses import dataclass
from pymongo import MongoClient
from src.Turbo_Engine_Predict_Maintenance.logger import logging
from src.Turbo_Engine_Predict_Maintenance.exception import CustomException
from src.config import MONGODB_URI, DB_NAME, COLLECTION_NAMES
from src.Turbo_Engine_Predict_Maintenance.utils import connect_to_mongodb, fetch_data_from_mongodb, remove_id_field

@dataclass
class DataIngestionConfig:
    rul_data_path: str = os.path.join('artifacts', 'Rul.csv')
    train_data_path: str = os.path.join('artifacts', 'Train.csv')
    test_data_path: str = os.path.join('artifacts', 'Test.csv')

class DataIngestion:
    def __init__(self, uri, db_name, collection_names):
        self.uri = uri
        self.db_name = db_name
        self.collection_names = collection_names
        self.ingestion_config = DataIngestionConfig()

    def connect_to_mongodb(self):
        try:
            print(f"Connecting to MongoDB using URI: {self.uri}")
            client = MongoClient(self.uri)
            print(f"Selected database: {self.db_name}")
            self.db = client[self.db_name]
            self.collections = {name: self.db[name] for name in self.collection_names}
            print("Connected to MongoDB!")
        except Exception as e:
            raise CustomException(e, sys)

    def fetch_data_from_mongodb(self, collection_name):
        try:
            collection = self.collections[collection_name]
            all_documents = list(collection.find())

            # Remove the '_id' field from each document
            for document in all_documents:
                remove_id_field(document)

            df = pd.DataFrame(all_documents)
            return df
        except Exception as e:
            raise CustomException(e, sys)

    def save_data_to_csv(self, df, file_path):
        try:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            df.to_csv(file_path, index=False)
            print(f'Data saved to {file_path}')
        except Exception as e:
            raise CustomException(e)

    def initiate_data_ingestion(self):
        print('Data Ingestion start')
        try:
            # Connect to MongoDB
            self.connect_to_mongodb()

            # Fetch data from MongoDB and convert to DataFrame
            train_df = self.fetch_data_from_mongodb("Train")
            test_df = self.fetch_data_from_mongodb("Test")
            rul_df = self.fetch_data_from_mongodb("Rul")

            # Save the train and test and Rul data to CSV files
            self.save_data_to_csv(train_df, self.ingestion_config.train_data_path)
            self.save_data_to_csv(test_df, self.ingestion_config.test_data_path)
            self.save_data_to_csv(rul_df, self.ingestion_config.rul_data_path)

            print('Ingestion of Data is completed')

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
                self.ingestion_config.rul_data_path,
            )

        except Exception as e:
            print('Exception occurred at data ingestion stage')
            raise CustomException(e, sys)
