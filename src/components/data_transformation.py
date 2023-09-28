<<<<<<< HEAD
=======
#Importing libraries 
>>>>>>> 3d03f507d7572cba07c4152e349ede1e791ee838
import os 
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
import numpy as np
from dataclasses import dataclass
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import RobustScaler
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from src.utils import save_object

<<<<<<< HEAD
@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join("artifacts", "preprocessor.pkl")
    
    
class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
        
    def get_data_trasnformer_object(self):
        try:
=======
#Creating Data Transformation Config Class
@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join("artifacts", "preprocessor.pkl")

#Creating DataTransformation Class    
class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
        logging.info("Data Transformation Config Class initiated")
    
    #Function for Transforming the object    
    def get_data_trasnformer_object(self):
        try:
            logging.info("Data Transformation object selection class started")
>>>>>>> 3d03f507d7572cba07c4152e349ede1e791ee838
            num_cols = ['Engine_no', 'Cycle_no',
            'LPC_outlet_temperature',
            'HPC_outlet_temperature', 'LPT_outlet_temperature',
            'HPC_outlet_pressure',
            'Physical_fan_speed', 'Physical_core_speed', 
            'HPC_outlet_static_pressure', 'Fuel_flow_ratio', 'Fan_speed',
            'Bypass_ratio', 'Bleed_enthalpy',
            'High_pressure_cool_air_flow', 'Low_pressure_cool_air_flow']
<<<<<<< HEAD
            
=======
            logging.info("Numerical Cols defined")
            
            logging.info("Pipeline steps initiated for scaling & applying the PCA")
>>>>>>> 3d03f507d7572cba07c4152e349ede1e791ee838
            num_pipeline = Pipeline(
                
                steps = [
                    ("scaler", RobustScaler()),
<<<<<<< HEAD
                    ("PCA", PCA(n_components=8))
=======
                    ("PCA", PCA(n_components=0.95))
>>>>>>> 3d03f507d7572cba07c4152e349ede1e791ee838
                    
                ]
            )
            
            logging.info("Pipeline created")
            
<<<<<<< HEAD
=======
            logging.info("Preprocessor object creation started")
>>>>>>> 3d03f507d7572cba07c4152e349ede1e791ee838
            preprocessor = ColumnTransformer(
                
                [
                    ("num_pipeline", num_pipeline, num_cols)
                ]
            )
<<<<<<< HEAD
            
            return preprocessor
        
        except Exception as e:
            raise CustomException(e, sys)
        
    def initiate_data_transformation(self, train_path, test_path):
        
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            
            train_df["RUL"][train_df["RUL"] > 103] = 103
            test_df["RUL"][test_df["RUL"] > 103] = 103
            
            logging.info("Train & test data readed")
            
=======
            logging.info("Preprocessor object created")
            return preprocessor
        
        except Exception as e:
            logging.info("Error occur at getting transformation object")
            raise CustomException(e, sys)
    
    #  Function for initializing the data transformation  
    def initiate_data_transformation(self, train_path, test_path):
        
        try:
            logging.info("Reading of train & test data started")
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Reading of train & test data completed")
            
            train_df["RUL"][train_df["RUL"] > 103] = 103
            test_df["RUL"][test_df["RUL"] > 103] = 103
            logging.info("Function applied to train & test data")

            logging.info("Preprocessor object initiated for the train & test data")
            preprocessor_obj = self.get_data_trasnformer_object()
            
            logging.info("Columns defined for the data")
>>>>>>> 3d03f507d7572cba07c4152e349ede1e791ee838
            target_column_name = "RUL"
            drop_cols = [
                'Setting_1', 'Setting_2', 'Setting_3', 'Fan_inlet_temperature', 'Fan_inlet_pressure', 
                'Bypass_duct_pressure', 'Engine_pressure_ratio', 'Core_speed', 'Burner_fuel_air_ratio', 
<<<<<<< HEAD
                'Required_fan_speed', 'Required_fan_conversion_speed']  
            
            
=======
                'Required_fan_speed', 'Required_fan_conversion_speed']    
            
            logging.info("Feature selection & Target feature initiated for train & test data")
>>>>>>> 3d03f507d7572cba07c4152e349ede1e791ee838
            input_feature_train_df = train_df.drop(columns=[target_column_name] + drop_cols)
            target_feature_train_df = train_df[target_column_name]
            
            input_feature_test_df = test_df.drop(columns=[target_column_name] + drop_cols)
            target_feature_test_df = test_df[target_column_name]
<<<<<<< HEAD
            
            
            preprocessor_obj = self.get_data_trasnformer_object()
            logging.info("Applying preprocessing obj on train & test dataframe")
            
        #Transforming into Preprocessor object to data
            input_feature_train_arr = preprocessor_obj.fit_transform(input_feature_train_df) #train data
            input_feature_test_arr = preprocessor_obj.transform(input_feature_test_df) #test data
            logging.info("Preprocessing applied to training & test datasets") 
            
            #Converting into numpy array for train & test data
            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)] #train array 
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)] #test array
            logging.info("Data transfom into the array")
            
            #function from utils to save the preprocessor file
=======
            logging.info("Input & Target features defined for train & test data")
        
            
            logging.info("Applying preprocessing obj on train & test dataframe")
            input_feature_train_arr = preprocessor_obj.fit_transform(input_feature_train_df) 
            input_feature_test_arr = preprocessor_obj.transform(input_feature_test_df) 
            logging.info("Preprocessing applied to dataframe") 
            
            logging.info("Converting Preprocessor array into numpy array")
            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)] 
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)] 
            logging.info("Data transfom into the numpy array")
            
            #function from save the preprocessor file
            logging.info("Saving the Preprocessor object initialized")
>>>>>>> 3d03f507d7572cba07c4152e349ede1e791ee838
            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj = preprocessor_obj
            )
            logging.info("Preprocessor file saved as Pickle file")
            
<<<<<<< HEAD
=======
            logging.info("Data Transformation step completed")
>>>>>>> 3d03f507d7572cba07c4152e349ede1e791ee838
            return (
                train_arr,
                test_arr
            )
            
<<<<<<< HEAD
            
        except Exception as e:
=======
        except Exception as e:
            logging.info("Error occur at initializing the data Transformation step")
>>>>>>> 3d03f507d7572cba07c4152e349ede1e791ee838
            raise CustomException(e, sys)