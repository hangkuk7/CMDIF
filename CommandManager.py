import json
import requests

class CommandManager:
    def __init__(self):
        print('[CommandManager] init')
        self._url = None
        # default header setting
        self._header = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        self._rcmd_req_body = None
        self._rcmd_cmd = None
        self._rcmd_param = None
        self._request_body = None

    def set_cmd_url(self, url):
        self._url = url

    def set_cmd_header(self, headers):
        self._header = headers

    def set_rcmd_message(self, rcmd_prefix, rcmd_body):
        # double Json Encoding
        json_string = json.dumps(rcmd_body)
        json_string = json.dumps(rcmd_body)

        self._rcmd_cmd = '%s %s;' % (rcmd_prefix, json_string)

        return self._rcmd_cmd

    def make_command(self, req_params):

        json_req_params = json.dumps(req_params)

        return json_req_params

    def print_cmd_header(self):
        print(f'HEADER = [\n{self._header}\n]')

