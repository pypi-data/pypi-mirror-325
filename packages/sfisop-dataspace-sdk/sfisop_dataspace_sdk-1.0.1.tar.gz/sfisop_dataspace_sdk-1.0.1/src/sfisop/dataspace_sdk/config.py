import argparse
import os
from decouple import config
import yaml


class DataSpaceConfig:
    def __init__(self, baseurl, api_key):
        self.BASEURL = baseurl
        self.API_KEY = api_key

    def __str__(self) -> str:
        return ''.join((f'DataSpace Configuration: \n',
                        f'BASEURL: {self.BASEURL}'))


class DataSpaceConfigurationException(Exception):
    pass


def get_dataspace_config(config_file: str) -> DataSpaceConfig:

    try:
        with open(config_file) as f:
            conf = yaml.load(f, Loader=yaml.FullLoader)
            BASE_URL = conf['DATASPACE_BASE_URL']
            API_KEY_ID  = conf['DATASPACE_API_KEY_ID']

    except Exception as e:
        raise DataSpaceConfigurationException(f"Error when reading from config file: {e}")

    try:
        API_KEY = config(API_KEY_ID)

    except Exception as e:
        raise DataSpaceConfigurationException(f"Error when reading credentials from environment: {e}")

    dataspace_config = DataSpaceConfig(BASE_URL, API_KEY)

    return dataspace_config


def get_dataspace_configfile(description: str) -> str:
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--configfile", required=True, help="Path to the config file")
    args = parser.parse_args()

    if not os.path.exists(args.configfile):
        raise DataSpaceConfigurationException(f"Error: The configfile '{args.configfile}' does not exist.")

    return args.configfile

