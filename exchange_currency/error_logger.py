import logging
import traceback

logging.basicConfig(level=logging.ERROR)

def log_error(message, exception):
    try:
        """
        Logs an error message along with exception details and traceback.
        
        Parameters:
        message (str): Custom error message.
        exception (Exception): The caught exception to log.
        """
        logging.error(f"Error Message: {message}")
        logging.error(f"Exception: {str(exception)}")
        logging.error(f"Traceback: {traceback.format_exc()}")
    except Exception as e:
        print(f"Error Message: Error in log_error method")
        print(f"Exception: {str(e)}")
        print(traceback.format_exc())
