import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

## log file is my variable 
## inside this varibale datetime.now wil take current time, and remaining is the format of datetime
## .log = it will create everything in .log file format

log_path=os.path.join(os.getcwd(),"logs",LOG_FILE) ## from wherever im executing my file it will assume that as cwd and create log folder over there and log file will get store over
## log folder path
## getcwd( get current working dir)

## this is the path but i need to create folder also , so for this 
os.makedirs(log_path,exist_ok=True)  ## os.makedirs is a function

# step 1. we have set our log file name
# step 2. we have set our log file path
# step 3. then finally i have created folder

LOG_FILE_PATH=os.path.join(log_path,LOG_FILE)
## i have combined log file + log path, that will be my complete  log file path


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

## basic config is a function
# to make sure  where is the path and what is the format