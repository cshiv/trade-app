"""
This code can be used with Multi threaded approach for multiple users which
keeps running in the background.Set the EXECUTION_METHOD="MULTI_THREAD_BACKEND"

To run the code in web app mode which in turn uses flask set the EXECUTION_METHOD="WEBAPP"
"""

from controller.webapp import *
from controller.multi_threader import *
import logging


# Accepted Values MULTI_THREADED_BACKEND | WEBAPP
EXECUTION_METHOD="MULTI_THREAD_BACKEND"


def main():
    if EXECUTION_METHOD == "MULTI_THREAD_BACKEND":
        MultiThreadHandler.run_controller()
    elif EXECUTION_METHOD == "WEBAPP":
        pass
    else:
        logging.error("Set EXECUTION_METHOD to either MULTI_THREAD_BACKEND or WEBAPP ")
        exit -1

if __name__ == "__main__":
    main()