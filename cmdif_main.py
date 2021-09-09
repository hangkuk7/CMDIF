import json
from CommandManager import CommandManager

def request_getBtsInformation(api_url, api_headers, api_data):
    print(f'request_getBtsInformation() start')
    print(f'=========================== REQUEST ================================')
    print(f'api_url=[{api_url}]')
    print(f'api_headers=[\n{api_headers}\n]')
    print(f'api_data=[\n{api_data}\n]')
    print(f'====================================================================')

    try:
        res = requests.post(api_url, data=api_data, headers=api_headers)
        res.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print(f'HTTP Error: {errh}')
    except requests.exceptions.ConnectionError as errc:
        print(f'Error Connecting: {errc}')
    except requests.exceptions.Timeout as errt:
        print(f'Timeout Error: {errt}')
    except requests.exceptions.RequestException as err:
        print(f'Something Else: {err}')

    json_response = res.json()
    print(f'=========================== RESPONSE================================')
    print(f'status code = [{res.status_code}]')
    print(f'header = [{res.headers}]')
    print(f'text=[\n{res.text}\n]')
    print(f'json=[\n{json_response}\n]')
    print(f'--------------------------------------------------------------------')
    print(f'elapsed=[{res.elapsed}]')
    print(f'====================================================================')

if __name__ == '__main__':
    print(f'main() start')

    # url = "http://10.6.176.179:10000/tspi/execute"
    #
    # headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    #
    # rcmd_body = {'requestId': 1, \
    #              'parameters': {'name': 'getBtsInformation'}
    #              }
    # json_string = json.dumps(rcmd_body)
    # json_string = json.dumps(json_string)
    #
    # rcmd_cmd = 'SEND-RCMD:246203, ' + json_string + ';'
    #
    # print(f'rcmd_cmd=[{rcmd_cmd}]')
    #
    # params = {'async': 0, \
    #           'requestId': '121212asdfasdf', \
    #           'callback': None, \
    #           'timeout': 60, \
    #           'username': 'nokia', \
    #           'password': '0743de26db4b619c60dafbf40ff17572', \
    #           'commond': rcmd_cmd
    #           }
    #
    # json_params = json.dumps(params)
    # print(f'json_params=[\n{json_params}\n]')

    # request_getBtsInformation(url, headers, json_params)
    cmd_mgr = CommandManager()

    # Set Url
    api_url = "http://10.6.176.179:10000/tspi/execute"
    cmd_mgr.set_cmd_url(api_url)
    cmd_mgr.print_cmd_url()