import sys ## sys will help  us to track error details

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error script name [{file_name}] line number [{exc_tb.tb_lineno}] error message [{str(error)}]" 


    #error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     #file_name,exc_tb.tb_lineno,str(error))

    return error_message




class CustomException(Exception):              ## error details types i have define with sys
    def __init__(self,error,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_details)

                        # i have defined a function over here ie;error_message detail 
                        # which will take the error message

    def __str__(self):
        return self.error_message  ## it will return error msg




## this class will inherit exception
## init - initialization constructor