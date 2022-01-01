from aryabhata.controller.zerodha_user import *
import aryabhata.app_config.zerodha_users as usercfg

# Initial testing
def multi_thread():
    user_handler = {}

    for user in usercfg.ZERODHA_USERS.keys():
        user_handler = ZerodhaUser(user)
        user_handler.generate_access_token()
        print(user_handler.get_access_token())
