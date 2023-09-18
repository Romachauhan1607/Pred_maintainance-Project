import os
import sys
from src.Turbo_Engine_Predict_Maintenance.logger import logging
from src.Turbo_Engine_Predict_Maintenance.exception import CustomException
import pandas as pd
from src.config import MONGODB_URI, DB_NAME, COLLECTION_NAMES
from src.Turbo_Engine_Predict_Maintenance.components.data_ingestion import DataIngestion
from src.Turbo_Engine_Predict_Maintenance.components.data_transformation import DataTransformation
from src.Turbo_Engine_Predict_Maintenance.components.model_trainer import ModelTrainer




if __name__ == '__main__':
    obj = DataIngestion(MONGODB_URI, DB_NAME, COLLECTION_NAMES)
    train_data_path,test_data_path,rul_data_path = obj.initiate_data_ingestion()
    data_transformation = DataTransformation()
    train_arr,test_arr,_ = data_transformation.initiate_data_transformation(train_data_path,test_data_path,rul_data_path)
    model_trainer = ModelTrainer()
    model_trainer.initiate_model_training(train_arr,test_arr)