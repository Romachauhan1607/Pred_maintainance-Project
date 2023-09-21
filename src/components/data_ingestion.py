import os 
import sys
import time
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass
from src.utils import read_sql_data


#Data Ingestion Config
@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join("artifacts", "train.csv")
    logging.info("Train file loaded")
    test_data_path:str = os.path.join("artifacts", "test.csv")
    logging.info("Test file loaded")



class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        try:
            df = read_sql_data()
            logging.info("Reading from SQL database")
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok = True)
            os.makedirs(os.path.dirname(self.ingestion_config.test_data_path), exist_ok = True)
            
            df[0].to_csv(self.ingestion_config.train_data_path, index = False, header = True)
            df[1].to_csv(self.ingestion_config.test_data_path, index = False, header = True)
            
            logging.info("Data Ingestion Completed")
            
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)