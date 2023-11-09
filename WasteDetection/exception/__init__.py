import sys 

#below create an error function which use system module to find in which line it got the error

def error_message_detail(error,error_detail:sys):
    _,_, exc_tb=error_detail.exc_info()

    file_name=exc_tb.tb_frame.f_code.co_filename

    error_message="Error occured python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )
    return error_message

# in this I inherit my custom exception by the arg 'Exception' which is inbuilt custom exception module in python
class AppException(Exception):
    def __init__(self,error_message,error_detail):
        """
        :param error_message: error message in string format
        """

        super().__init__(error_message)

        self.error_message=error_message_detail(
            error_message,error_detail=error_detail #here we call
        ) 

    def __str__(self):
        return self.error_message