import sys
from networdsecurity.logging import logger

 
class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details:sys):
        self.error_message = error_message
        _,_,exc_tb = error_details.exc_info() # First two information is not required so we denote as _,_, to discard them

        self.lineno = exc_tb.tb_lineno
        self.file_nane = exc_tb.tb_frame.f_code.co_filename

    
    def __str__(self):
        return "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
            self.file_nane, self.lineno, str(self.error_message)
        )
    
if __name__ == '__main__':
    try:
        logger.logging.info("Enter the try block")
        a=1/0
        print("This will not be printed",a)
    except Exception as e:
        raise NetworkSecurityException(e, sys)