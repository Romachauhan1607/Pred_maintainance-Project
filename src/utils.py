import os 
import sys
#import dill
import pymysql
from src.exception import CustomException
from src.logger import logging
import pandas as pd
import pickle
from sklearn.metrics import r2_score


host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")

#Reading SQL data 
def read_sql_data():
    logging.info("Reading SQL Database")
    
    try:
        mydb = pymysql.connect(
            host = host,
            user = user,
            password = password,
            db = db
        )
        logging.info("Connection establish")
        
        df_train = pd.read_sql_query("select * from train1", mydb)
        logging.info("Train readed")
        df_test = pd.read_sql_query("select * from test1", mydb)
        logging.info("Test readed")
        
        return df_train, df_test
        
    except Exception as e:
        raise CustomException(e, sys)
    
    
def save_object(file_path, obj):
    
    try:
        dir_path = os.path.dirname(file_path)
        
        os.makedirs(dir_path, exist_ok = True)
        
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
                   
    except Exception as e:
        raise CustomException(e, sys)
    
def evaluate_models(X_train, y_train,X_test,y_test,models):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]

            model.fit(X_train,y_train)  # Train model

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())]
        
    except Exception as e:
        raise CustomException(e, sys)
    

def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)