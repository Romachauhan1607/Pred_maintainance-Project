import os 
import sys
import pymysql
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from dataclasses import dataclass


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