import json
import requests

class CommandManager:
    def __init__(self):
        print('[CommandManager] init')
        self._url = None
        # default header setting
        self._req_header = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        self._rcmd_req_body = None
        self._rcmd_cmd = None
        self._request_body = None
        self._http_res_code = None
        self._res_header = None
        self._res_text = None
        self._elapsed_time = None

    def set_cmd_url(self, url):
        self._url = url

    def set_cmd_req_header(self, headers):
        self._req_header = headers

    def set_rcmd_message(self, rcmd_prefix, rcmd_body):
        # double Json Encoding
        tmp_json_string = json.dumps(rcmd_body)
        json_string = json.dumps(tmp_json_string)

        self._rcmd_cmd = '%s, %s;' % (rcmd_prefix, json_string)

        return self._rcmd_cmd

    def make_command(self, req_params):

        self._request_body = json.dumps(req_params)

        return self._request_body

    def send_command(self):
        print(f'[CommandManager] send_command() start')
        print(f'=========================== REQUEST ================================')
        print(f'api_url=[{self._url}]')
        print(f'api_headers=[\n{self._req_header}\n]')
        print(f'api_body=[\n{self._request_body}\n]')
        print(f'====================================================================')

        try:
            res = requests.post(
                self._url,
                data=self._request_body,
                headers=self._req_header,
                timeout=600)
            res.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            print(f'HTTP Error: {errh}')
            return False
        except requests.exceptions.ConnectionError as errc:
            print(f'Error Connecting: {errc}')
            return False
        except requests.exceptions.Timeout as errt:
            print(f'Timeout Error: {errt}')
            return False
        except requests.exceptions.RequestException as err:
            print(f'Something Else: {err}')
            return False

        self._http_res_code = str(res.status_code)
        self._res_header = res.headers
        self._res_text = res.text
        self._elapsed_time = res.elapsed

        print(f'=========================== RESPONSE================================')
        print(f'status code = [{self._http_res_code}]')
        print(f'header = [{self._res_header}]')
        print(f'text=[\n{self._res_text}\n]')
        print(f'--------------------------------------------------------------------')
        print(f'elapsed time=[{self._elapsed_time}]')
        print(f'====================================================================')

        return True

    def print_cmd_url(self):
        print(f'URL = [\n{self._url}\n]')

    def print_cmd_req_header(self):
        print(f'REQUEST HEADER = [\n{self._req_header}\n]')

    def get_command_result(self):
        return self._http_res_code, self._res_text

