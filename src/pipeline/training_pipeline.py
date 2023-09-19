#Defining components from source components
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

from src.exception import CustomException
from src.logger import logging
import sys

#Initiating Training Pipeline with connecting the components
try: 
    if __name__ == "__main__": 
        
        logging.info("Training Pipeline initiated")
        obj = DataIngestion() 
        train_data_path, test_data_path = obj.initiate_data_ingestion() 
        logging.info("Data Ingestion step Completed") 
    
        logging.info("Data Transformation Step initated")
        data_transformation = DataTransformation()
        train_arr, test_arr = data_transformation.initiate_data_transformation(train_data_path, test_data_path) 
        logging.info("Data Transformation step completed")
        
        logging.info("Model Trainer step initiated")
        model_trainer=ModelTrainer()
        model_trainer.initiate_model_training(train_arr,test_arr)
        logging.info("Model Trainer step completed")
        
        logging.info("Training Pipeline completed sucessfully")   

except Exception as e:
    logging.info("Error occured in Training Pipeline")
    raise CustomException(e, sys)
 