import boto3
import logging


class AWSSSMUtils:
    AWS_DEFAULT_REGION = "ap-south-1"
    AWS_SSM_BOTO_ID = "ssm"
    ssm_handler = None

    def __init__(self):
        logging.debug("Initialized SSM")
        pass

    @classmethod
    def get_value(cls,name, region=AWS_DEFAULT_REGION):
        try:
            ssm_handler = boto3.client(AWSSSMUtils.AWS_SSM_BOTO_ID, region)
            val = ssm_handler.get_parameter(Name=name, WithDecryption=True)["Parameter"]["Value"]
            logging.info("Fetched Parameter " + name + " from SSM")
        except Exception as e:
            logging.error("Exception in getting SSM parameter %s", name)
            raise e
        return val

    @classmethod
    def set_value(cls,name, value, type='SecureString', region=AWS_DEFAULT_REGION):
        try:
            ssm_handler = boto3.client(AWSSSMUtils.AWS_SSM_BOTO_ID, region)
            retValue = ssm_handler.put_parameter(Name=name, Value=value, Type=type, Overwrite=True)
        except Exception as e:
            logging.error("Exception in putting SSM parameter %s with value %s", name, value)
            raise e
