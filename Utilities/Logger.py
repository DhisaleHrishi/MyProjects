import inspect
import logging

class Login_Class:
    @staticmethod
    def log_generator():
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        logfile = logging.FileHandler("C:\\Users\\GURUDEV\\PycharmProjects\\OpenCart_Project\\Logs\\OpenCartLogFile.log")
        format = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(funcName)s - %(message)s")
        logfile.setFormatter(format)
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger

#file
#format
#file --> Format
#add log
#log level

#info
#debug
#warning
#error
#critical
