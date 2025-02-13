import requests
import datetime
import urllib


class DataSpaceClient:

    def __init__(self, dataspace_config):
        self.base_url = dataspace_config.BASEURL
        self.api_key = dataspace_config.API_KEY

    def send_request(self, path):

        url = self.base_url + '/' + path

        headers = {
            'X-API-Key': self.api_key,
            'accept': 'application/json'
        }

        response = requests.request("GET", url, headers=headers)

        return response

    def get_latest(self, datasource):

        response = self.send_request(f'smartocean/{datasource}/sensors/latest')

        return response

    def get_period(self, datasource, start: datetime.datetime, end: datetime.datetime):

        # TODO: validate that start is earlier than end
        start_time = urllib.parse.quote(start.isoformat())
        end_time = urllib.parse.quote(end.isoformat())

        response = self.send_request(f'smartocean/{datasource}/sensors/?start={start_time}&end={end_time}')

        return response


