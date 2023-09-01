import requests


class Session:
    def __init__(self) -> None:
        self.sessiion = requests.Session()
