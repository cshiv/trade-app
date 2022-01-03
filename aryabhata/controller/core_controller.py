import logging
from aryabhata.user_handlers.zerodha_user import *

class Controller:
    def __init__(self,user):
        self.user = user
        logging.info("Initiated central controller for %s" %(self.user))

    def init_control(self):
        self.user_login()
        self.run_algo()

    def user_login(self):
        self.broker_handler = ZerodhaUser(self.user)
        self.broker_handler.generate_access_token()
        #print("Token %s generated for user %s" %(self.broker_handler.get_access_token(),self.user))

    def run_algo(self):
        logging.info("Running Algo")
        pass



