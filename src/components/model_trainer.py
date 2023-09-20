#importing libraries
import os 
import sys
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import GradientBoostingRegressor
from src.utils import save_object
from src.utils import evaluate_model

#Defining class for Model Trainer confing
@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts", "model.pkl")
    
class ModelTrainer:
    logging.info("Model Trainer Step initialized")
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()
        logging.info("Model Trainer config initiated")
        
    logging.info("Model Training step initiated")   
    def initiate_model_training(self, train_array, test_array):
        try:
            logging.info("Train data & Test Data defined step initiated")
            X_train, y_train, X_test, y_test = (
                train_array[:,:-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1]
            )
            logging.info("Train & test data defined")
            
            logging.info("Different Model provided for the given data")
            models = {
                
                "LinearRegression" : LinearRegression(),
                "SVR" : SVR(),
                "RandomForest" : RandomForestRegressor(),
                "KNN" : KNeighborsRegressor(),
                "DecisionTree" : DecisionTreeRegressor(),
                "GradientBoosting" : GradientBoostingRegressor()
            }
            
            logging.info("Hyperparameter extracted to the respective models")
            params = {
                
                "LinearRegression" : {},
                
                "SVR" : {
                    'epsilon': [0.1, 0.2],
                    'kernel': ['rbf', 'linear', 'poly'],
                    'degree': [3 , 5],
                },
                
                "RandomForest" :{
                    
                    'criterion':['squared_error', 'absolute_error'],                 
                    'max_features':['sqrt','log2',None],
                    'n_estimators': [8,64,256]
                },
                
                "KNN" : {
                    
                    'n_neighbors' : [5, 11],
                    'weights' : ['uniform', 'distance'],
                    'algorithm' : ['auto', 'brute']
                },
                
                "DecisionTree" : {
                    'criterion' : ['absolute_error', 'poisson'],
                    'splitter' : ['best', 'random'],
                    'max_features':['sqrt','log2']
                },
                
                "GradientBoosting" : {
                    
                    'loss':['squared_error', 'absolute_error'],
                    'learning_rate':[0.1,.05],
                    'criterion':['squared_error', 'friedman_mse'],
                    'n_estimators': [8,256]
                }
                
                
            }
            logging.info("Hyperparameter assigning completed")
            
            logging.info("Model Evaluating step started")
            model_report:dict=evaluate_model(X_train, y_train, X_test, y_test, models,params)
            print(model_report) 
            print("\n")
            logging.info(f"Model Report : {model_report}")
            
            best_model_score = max(sorted(model_report.values()))
            logging.info("Model score sorted")
            
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            logging.info("Best model name has been found")
            
            best_model = models[best_model_name]
            print(f"Best Model is {best_model_name} with accuracy : {best_model_score}")
            print("\n*****")
            logging.info(f"Best Model is {best_model_name} with accuracy : {best_model_score}")
            
            logging.info("Model Saving step initiated")
            save_object(   
                file_path = self.model_trainer_config.trained_model_file_path, #storing file path
                obj = best_model
            )
            logging.info("Best model saved as pkl file")
            

        except Exception as e:
            logging.info("Error occured at Model Training Step")
            raise CustomException(e, sys)