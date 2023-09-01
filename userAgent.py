import json


class UserAgent:
    def __init__(self, ua: str, pct: float) -> None:
        self.ua: str = ua
        self.pct: float = pct
        self.isActive: bool = False
