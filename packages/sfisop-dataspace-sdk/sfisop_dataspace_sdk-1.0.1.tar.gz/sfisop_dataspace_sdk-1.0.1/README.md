# Data Space Service Client SDK

Basic client library for accessing the SmartOcean data space service to retrieve historical time series data from data sources.

## Data Space Service REST API

The SmartOcean dataspace service provides a REST API. 

# Sample Client Code

A sample implementation of the client-side code is provided in the `main.py` file. 

```python
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
```

It can be executed as:

```bash
python client.py <path-to-configuration-file>
```

The code is to be used as a starting point for the implementation of the client applications.

A configuration file that can be used for the SmartOcean data space service can be found in the configs folder.

The data sources are currently available on the SmartOcean platform for demonstration purposes can be found in the `sop_datasources.py` file.

# Configuration and credentials        

The configuration file provided as on the command-line must contain the following information:

```
DATASPACE_BASE_URL: <base-url-for-dataspace-service>
DATASPACE_API_KEY_ID: DATASPACE_API_KEY
```

where the `DATASPACE_API_KEY` is the API key identifier that is contained in an `.env` file that must contain the following information:

```
DATASPACE_API_KEY = '<api-key>'
```

This indirect configuration of the API key makes it possible to share a single `.env` file for credentials across different deployments of the data space service.

The API key must be obtained from the SmartOcean data space service.
