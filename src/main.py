"""
This code can be used with Multi threaded approach for multiple users which
keeps running in the background.Set the EXECUTION_METHOD="MULTI_THREAD_BACKEND"

To run the code in web app mode which in turn uses flask set the EXECUTION_METHOD="WEBAPP"
"""

from controller.webapp import *
from  controller.multi_threader import *
import logging

# Accepted Values MULTI_THREADED_BACKEND | WEBAPP
EXECUTION_METHOD="MULTI_THREAD_BACKEND"

if __name__ == "__main__":
    if EXECUTION_METHOD == "MULTI_THREAD_BACKEND":
        multi_thread()
    elif EXECUTION_METHOD == "WEBAPP":
        webapp()
    else:
        logging.error("SetEXECUTION_METHOD to either MULTI_THREAD_BACKEND or WEBAPP ")
        exit -1


