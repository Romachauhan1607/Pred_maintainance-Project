<<<<<<< HEAD
from src.logger import logging
=======
#Defining components from source components
>>>>>>> 3d03f507d7572cba07c4152e349ede1e791ee838
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

<<<<<<< HEAD
if __name__ == "__main__":
    
    data_ingestion = DataIngestion()
    train_data, test_data = data_ingestion.initiate_data_ingestion()
    
    data_transformation = DataTransformation()
    train_array, test_array = data_transformation.initiate_data_transformation(train_data, test_data)
    
    model_trainer = ModelTrainer()
    model_trainer.initiate_model_training(train_array, test_array)   
=======
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
 
>>>>>>> 3d03f507d7572cba07c4152e349ede1e791ee838
