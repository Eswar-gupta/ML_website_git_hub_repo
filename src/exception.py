import sys
from src.logger import logging

# Hear error_detail:sys is nothing but deflaut parameter decalration you can also pass trackables and some other modules or objects of same fuction as a module
def error_message_details(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    line_number = exc_tb.tb_lineno
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in file name [{0}] and in line number [{1}] the error message is [{2}]".format(file_name, line_number,str(error))

    return error_message

#super is used to initialize the init of the paprent class

class CustomException(Exception):
    def __init__(self,error,error_details:sys):
        super().__init__(error) #just passing the error to the exception class's init so that some inbuilt thing will be done

        self.error_message = error_message_details(error,error_detail = error_details)

    def __str__(self):
        return self.error_message
    
