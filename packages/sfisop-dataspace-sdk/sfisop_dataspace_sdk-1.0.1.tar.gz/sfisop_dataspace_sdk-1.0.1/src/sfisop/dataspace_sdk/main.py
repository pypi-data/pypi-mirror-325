import datetime

from sfisop.dataspace_sdk.client import DataSpaceClient
from sfisop.dataspace_sdk.config import get_dataspace_config, get_dataspace_configfile
from sfisop.dataspace_sdk import sop_datasources as data_sources

if __name__ == '__main__':

    config_file = get_dataspace_configfile("DataSpace Configuration")
    dataspace_config = get_dataspace_config(config_file)

    client = DataSpaceClient(dataspace_config)

    response_latest = client.get_latest(data_sources.HVLVIRTUAL)
    print(response_latest.status_code)
    print(response_latest.text)

    start_time = datetime.datetime(2024, 6, 1, 0, 0, 0)
    end_time = datetime.datetime(2024, 6, 7, 0, 0, 0)

    response_period = client.get_period(data_sources.HVLVIRTUAL, start_time, end_time)
    print(response_period.status_code)
    print(response_period.text)
