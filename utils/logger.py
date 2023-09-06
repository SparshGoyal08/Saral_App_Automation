import inspect
import logging

import allure


def customLogger():
    """
    Custom logger method that stores logs for all the steps
    :return: logger
    """
    # This is used to get the  class / method name from where this customLogger method is called
    logName = inspect.stack()[1][3]

    # Create the logging object and pass the logName in it
    logger = logging.getLogger(logName)

    # Set the Log level
    logger.setLevel(logging.DEBUG)

    # Create the fileHandler to save the logs in the file
    fileHandler = logging.FileHandler("C:/Users/DELL/Saral_App_Automation/LocalLogs/TestRunLogs.log", mode='a', encoding="utf-8")

    # Set the logLevel for fileHandler
    fileHandler.setLevel(logging.DEBUG)

    # Create the formatter in which format do you like to save the logs
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s',
                                  datefmt='%d/%m/%y %I:%M:%S %p %A')

    # Set the formatter to fileHandler
    fileHandler.setFormatter(formatter)

    # Add file handler to logging
    logger.addHandler(fileHandler)

    # Finally return the logging object
    return logger


def allureLogs(text):
    with allure.step(text):
        pass
