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

<<<<<<< HEAD
=======
#Defining class for Model Trainer confing
>>>>>>> 3d03f507d7572cba07c4152e349ede1e791ee838
@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts", "model.pkl")
    
class ModelTrainer:
<<<<<<< HEAD
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()
        
    def initiate_model_training(self, train_array, test_array):
        try:
            #Separating Train & test array
=======
    logging.info("Model Trainer Step initialized")
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()
        logging.info("Model Trainer config initiated")
        
    logging.info("Model Training step initiated")   
    def initiate_model_training(self, train_array, test_array):
        try:
            logging.info("Train data & Test Data defined step initiated")
>>>>>>> 3d03f507d7572cba07c4152e349ede1e791ee838
            X_train, y_train, X_test, y_test = (
                train_array[:,:-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1]
            )
<<<<<<< HEAD
            
=======
            logging.info("Train & test data defined")
            
            logging.info("Different Model provided for the given data")
>>>>>>> 3d03f507d7572cba07c4152e349ede1e791ee838
            models = {
                
                "LinearRegression" : LinearRegression(),
                "SVR" : SVR(),
                "RandomForest" : RandomForestRegressor(),
                "KNN" : KNeighborsRegressor(),
                "DecisionTree" : DecisionTreeRegressor(),
                "GradientBoosting" : GradientBoostingRegressor()
            }
            
<<<<<<< HEAD
=======
            logging.info("Hyperparameter extracted to the respective models")
>>>>>>> 3d03f507d7572cba07c4152e349ede1e791ee838
            params = {
                
                "LinearRegression" : {},
                
                "SVR" : {
<<<<<<< HEAD
                    'kernel': ['linear', 'poly'],
                    'epsilon': [0.1, 0.2],
=======
                    'epsilon': [0.1, 0.2],
                    'kernel': ['rbf', 'linear', 'poly'],
                    'degree': [3 , 5],
>>>>>>> 3d03f507d7572cba07c4152e349ede1e791ee838
                },
                
                "RandomForest" :{
                    
                    'criterion':['squared_error', 'absolute_error'],                 
<<<<<<< HEAD
                    'max_features':['sqrt','log2'],
=======
                    'max_features':['sqrt','log2',None],
                    'n_estimators': [8,64,256]
>>>>>>> 3d03f507d7572cba07c4152e349ede1e791ee838
                },
                
                "KNN" : {
                    
<<<<<<< HEAD
                    'n_neighbors' : [5, 7],
                    'weights' : ['uniform', 'distance'],
=======
                    'n_neighbors' : [5, 11],
                    'weights' : ['uniform', 'distance'],
                    'algorithm' : ['auto', 'brute']
>>>>>>> 3d03f507d7572cba07c4152e349ede1e791ee838
                },
                
                "DecisionTree" : {
                    'criterion' : ['absolute_error', 'poisson'],
<<<<<<< HEAD
=======
                    'splitter' : ['best', 'random'],
>>>>>>> 3d03f507d7572cba07c4152e349ede1e791ee838
                    'max_features':['sqrt','log2']
                },
                
                "GradientBoosting" : {
                    
                    'loss':['squared_error', 'absolute_error'],
<<<<<<< HEAD
                    'criterion':['squared_error', 'friedman_mse'],
=======
                    'learning_rate':[0.1,.05],
                    'criterion':['squared_error', 'friedman_mse'],
                    'n_estimators': [8,256]
>>>>>>> 3d03f507d7572cba07c4152e349ede1e791ee838
                }
                
                
            }
<<<<<<< HEAD
            
            model_report:dict=evaluate_model(X_train, y_train, X_test, y_test, models,params)
            print(model_report) 
            print("\n**********")
=======
            logging.info("Hyperparameter assigning completed")
            
            logging.info("Model Evaluating step started")
            model_report:dict=evaluate_model(X_train, y_train, X_test, y_test, models,params)
            print(model_report) 
            print("\n")
>>>>>>> 3d03f507d7572cba07c4152e349ede1e791ee838
            logging.info(f"Model Report : {model_report}")
            
            best_model_score = max(sorted(model_report.values()))
            logging.info("Model score sorted")
            
<<<<<<< HEAD
            #finding best model name
=======
>>>>>>> 3d03f507d7572cba07c4152e349ede1e791ee838
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            logging.info("Best model name has been found")
            
            best_model = models[best_model_name]
            print(f"Best Model is {best_model_name} with accuracy : {best_model_score}")
            print("\n*****")
            logging.info(f"Best Model is {best_model_name} with accuracy : {best_model_score}")
            
<<<<<<< HEAD
=======
            logging.info("Model Saving step initiated")
>>>>>>> 3d03f507d7572cba07c4152e349ede1e791ee838
            save_object(   
                file_path = self.model_trainer_config.trained_model_file_path, #storing file path
                obj = best_model
            )
            logging.info("Best model saved as pkl file")
            

        except Exception as e:
<<<<<<< HEAD
=======
            logging.info("Error occured at Model Training Step")
>>>>>>> 3d03f507d7572cba07c4152e349ede1e791ee838
            raise CustomException(e, sys)