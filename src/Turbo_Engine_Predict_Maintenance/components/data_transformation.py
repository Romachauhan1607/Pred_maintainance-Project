import os
import sys
import numpy as np
import pandas as pd
from sklearn.preprocessing import RobustScaler
from sklearn.decomposition import PCA  # Import PCA
from src.Turbo_Engine_Predict_Maintenance.logger import logging
from src.Turbo_Engine_Predict_Maintenance.exception import CustomException
from dataclasses import dataclass
from src.Turbo_Engine_Predict_Maintenance.utils import RULCalculator, save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', 'preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
    
    def initiate_data_transformation(self, train_path, test_path, rul_path):
        try:
            # Reading train, test, and rul data
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            rul_df = pd.read_csv(rul_path)

            logging.info('Read train and test data and rul data')

            # Calculate RUL and add it to train and test data
            rul_calculator = RULCalculator(train_df, test_df, rul_df)
            train_df_with_rul = rul_calculator.add_rul_to_train_data()
            test_df_with_rul = rul_calculator.add_rul_to_test_data_with_rul_df()

            # 
            train_df_with_rul["RUL"][train_df_with_rul["RUL"] > 103] = 103
            test_df_with_rul["RUL"][test_df_with_rul["RUL"] > 103] = 103

            logging.info(f'Train Dataframe head: \n{train_df_with_rul.head().to_string()}')
            logging.info(f'Test Dataframe head: \n{test_df_with_rul.head().to_string()}')

            target_column_name = 'RUL'
            drop_columns = ['op_setting_1', 'op_setting_2', 'op_setting_3', 'sensor_measurement1', 'sensor_measurement5', 'sensor_measurement6', 'sensor_measurement10',
                'sensor_measurement14', 'sensor_measurement16', 'sensor_measurement18', 'sensor_measurement19','RUL']

            input_feature_train_df = train_df_with_rul.drop(columns=drop_columns, axis=1)
            target_feature_train_df = train_df_with_rul[target_column_name]

            input_feature_test_df = test_df_with_rul.drop(columns=drop_columns, axis=1)
            target_feature_test_df = test_df_with_rul[target_column_name]

            # Transforming using RobustScaler
            scaler = RobustScaler()
            input_feature_train_arr = scaler.fit_transform(input_feature_train_df)
            input_feature_test_arr = scaler.transform(input_feature_test_df)
            logging.info("Scaling input features")

            # Apply PCA
            pca = PCA(n_components=input_feature_train_arr.shape[1])  # Adjust the number of components as needed
            input_feature_train_arr_pca = pca.fit_transform(input_feature_train_arr)
            input_feature_test_arr_pca = pca.transform(input_feature_test_arr)
            logging.info("Applied PCA to reduce dimensionality")

            # Display feature names after PCA
            pca_feature_names = [f"PCA_{i+1}" for i in range(input_feature_train_arr_pca.shape[1])]
            print(pca_feature_names)
            logging.info(f'PCA Feature Names: {pca_feature_names}')

            train_arr = np.c_[input_feature_train_arr_pca, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr_pca, np.array(target_feature_test_df)]

            # Display the first few rows of the NumPy arrays
            logging.info(f'Train Array head: \n{train_arr[:5]}')
            logging.info(f'Test Array head: \n{test_arr[:5]}')


            # Save the preprocessor object (scaler)
            save_object(file_path=self.data_transformation_config.preprocessor_obj_file_path, obj=pca)
            logging.info("Data transformation successful")
            
            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
            
        except Exception as e:
            logging.info("Exception occurred in the initiate_data_transformation")
            raise CustomException(e, sys)