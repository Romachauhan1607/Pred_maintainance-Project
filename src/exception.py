import sys 

#Defining the type of error message & details we want
<<<<<<< HEAD
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))

    return error_message


class CustomException(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_details)

    def __str__(self):
        return self.error_message
=======
def error_message_detail(error,error_detail:sys): 
    _,_,exc_tb = error_detail.exc_info() 
    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = f"Error script name [{file_name}] line number [{exc_tb.tb_lineno}] error message [{str(error)}]" 

#Logging Error message which log the details
class CustomException(Exception):    
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self): 
        return self.error_message  
>>>>>>> 3d03f507d7572cba07c4152e349ede1e791ee838
