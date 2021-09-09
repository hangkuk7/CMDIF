import json
import requests

class CommandManager:
    def __init__(self):
        print('[CommandManager] init')
        self._url = None
        # default header setting
        self.header = {'Accept': 'application/json', 'Content-Type': 'application/json'}