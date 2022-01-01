import logging
from kiteconnect import KiteConnect
import requests
import time
from aws_ssm import AWSSSMUtils as aws_ssm
import alpha.src.global_config.brokers as brokers


class ZerodhaUser():

    HTTP_SUCCESS_STATUS = 200
    DELAY_MFA_AUTH_TIME = 2 # Delay MFA auth for 2 secs to simulate manual behaviour
    LOGIN_ERROR_CODE = -1
    MFA_ERROR_CODE = -2

    def __init__(self,user):
        self.zerodha_config = brokers.BROKERS["zerodha"]
        user_details=self.load_user_details(user)
        logging.debug("Zerodha Broker config is %s", str(self.zerodha_config))
        self.user = user_details["user"]
        self.password = user_details["password"]
        self.mfa = user_details["mfa"]
        self.api_key = user_details["api_key"]
        self.api_secret = user_details["api_secret"]
        self.access_token = user_details["access_token"]
        self.kite = None
        try:
            self.kite = self.init_kite_connect()
        except Exception as e:
            raise e

    def init_kite_connect(self):
        try:
            kite = KiteConnect(api_key=self.api_key)
            return kite
        except Exception as e:
            logging.error("Error getting kite connect instance for user %s",self.user)
            logging.error(e)
            raise e

    def load_user_details(self):
        user_details = {}
        fields = ["user","password","mfa","api_key","api_secret","access_token"]
        for item in fields:
            user_details[item]=aws_ssm.get_value("/"+"/".join([self.zerodha_config["name"]+self.user+item]))
        return user_details

    def get_zerodha_config(self):
        return self.zerodha_config

    def generate_request_token(self):
        try:
            s = requests.Session()
            res = s.post(self.zerodha_config["login_url"],
                         {"user_id": self.user, "password": self.password},
                         timeout=self.zerodha_config["login_timeout"])
            if res.status_code != self.HTTP_SUCCESS_STATUS:
                return self.LOGIN_ERROR_CODE
            request_id = eval(res.text)["data"]["request_id"]
            logging.info("Logged in with user %s",self.user)
            time.sleep(self.DELAY_MFA_AUTH_TIME)
            res = s.post(self.zerodha_config["mfa_url"],
                         {"user_id": self.user, "request_id": request_id, "twofa_value": self.mfa},
                         timeout=self.zerodha_config["login_timeout"])
            if res.status_code != self.HTTP_SUCCESS_STATUS:
                return self.MFA_ERROR_CODE
            logging.info("MFA successful for user %s",self.user)
            res= s.get(self.zerodha_config["request_token_url"]+self.api_key,
                       timeout=self.zerodha_config["login_timeout"])
            tmp = (res.url).split("request_token=")
            request_token = tmp[1].split("&")
            logging.info("Fetched Request token for user %s",self.user)
            return request_token
        except Exception as e:
            logging.error("Error in login to Zerodha or MFA")
            logging.error(e)
            raise e

    """
        generate_access_token: Generate access token from scratch. Action includes logging to Zerodha and generating access token
        This method can also be used for call back for Token expiry handling.
    """
    def generate_access_token(self):
        try:
            request_token = self.generate_request_token()
            data = self.kite.generate_session(request_token, self.api_secret)
            access_token = data['access_token']
            aws_ssm.set_value("access_token",access_token)
            return access_token
        except Exception as e:
            logging.error("Error generating access token for user %s",self.user)
            logging.error(e)
            raise e

    def get_access_token(self):
        return self.access_token

