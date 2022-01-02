from aryabhata.user_handlers.zerodha_user import *
import aryabhata.app_config.zerodha_users as usercfg
from aryabhata.controller.core_controller import *
import threading


class MultiThreadHandler:
    user_handler = {}
    controls = {}
    threads = {}

    def __init__(self):
        logging.info("Initialized MultiThread Handler") # Need to populate it later

    @classmethod
    def run_controller(cls):
        for user in usercfg.ZERODHA_USERS.keys():
            MultiThreadHandler.controls[user] = Controller(user)
            MultiThreadHandler.threads[user] = threading.Thread(target=MultiThreadHandler.controls[user].init_control)
            MultiThreadHandler.threads[user].start()
