import logging


class Controller:
    def __init__(self,user):
        self.user = user
        logging.info("Initiated central controller for %s" %(self.user))


